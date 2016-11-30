

# Internet Measurements #
>CS425: Computer Networking (Project-5)
						
* Analyzed publicly-available measurement data to understand important properties of the Internet.
* **Traffic Measurement:** Five-minute trace of Netflow records captured from a router in the [Internet2][l1] backbone that connects the major research universities in the United States is recoreded in csv file. 
* **BGP Measurement:** BGP update messages logged by [RouteViews][l2] to analyze BGP (in)stability and convergence behavior. RouteViews has BGP sessions with a variety of different ISPs, and logs the update messages sent on each of these sessions. The update files log BGP updates for each 15-minute interval, and the RIB files have the periodic routing-table (Routing Information Base) dumps.
* Python Scripts are used to plot complementary cumuluative distribution function(ccdf) and to calculate various fractions in traffic and BGP measurement.
* Refer to `project5-desc.pdf` and `Final_Report.pdf` for more details.

### Requirements ###
* `flow.2001-09-29.csv.gz` : Contains `ft-v05.2010-09-29.235501+0000.csv` flow record file for traffic measurement.
* `updates-asst4.tar.gz` : Contains BGP update files in text format.
* `rib-asst4.tar.gz` : Contains RIB (Routing Information Base) files in text format.
* Python version 3.5.2 and python-packages: pandas, numpy, operator and matplotlib


[l1]: <http://www.internet2.edu/>
[l2]: <http://www.routeviews.org/>


