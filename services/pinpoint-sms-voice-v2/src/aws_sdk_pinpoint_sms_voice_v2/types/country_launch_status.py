"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#CountryLaunchStatus``."""

from typing import TypeAlias

"""<p>The per-country launch status of an RCS agent.</p> <ul> <li> <p> <code>CREATED</code>: The country launch has been created.</p> </li> <li> <p> <code>PENDING</code>: The country launch is pending.</p> </li> <li> <p> <code>PARTIAL</code>: The country launch is partially active.</p> </li> <li> <p> <code>ACTIVE</code>: The country launch is active.</p> </li> <li> <p> <code>REJECTED</code>: The country launch was rejected.</p> </li> </ul>"""
CountryLaunchStatus: TypeAlias = str
