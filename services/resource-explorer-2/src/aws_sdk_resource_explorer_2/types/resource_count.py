"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#ResourceCount``."""

from typing import TypedDict

from typing_extensions import NotRequired


class ResourceCount(TypedDict):
    total_resources: NotRequired["int"]
    """<p>The number of resources that match the search query. This value can't exceed 1,000. If there are more than 1,000 resources that match the query, then only 1,000 are counted and the <code>Complete</code> field is set to false. We recommend that you refine your query to return a smaller number of results.</p>"""
    complete: NotRequired["bool"]
    """<p>Indicates whether the <code>TotalResources</code> value represents an exhaustive count of search results.</p> <ul> <li> <p>If <code>True</code>, it indicates that the search was exhaustive. Every resource that matches the query was counted.</p> </li> <li> <p>If <code>False</code>, then the search reached the limit of 1,000 matching results, and stopped counting.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceCount) -> dict:
    out: dict = {}
    if "total_resources" in value:
        out["TotalResources"] = value["total_resources"]
    if "complete" in value:
        out["Complete"] = value["complete"]
    return out


def deserialize_json(data: dict) -> ResourceCount:
    out: ResourceCount = {}  # type: ignore[typeddict-item]
    if "TotalResources" in data:
        out["total_resources"] = data["TotalResources"]
    if "Complete" in data:
        out["complete"] = data["Complete"]
    return out
