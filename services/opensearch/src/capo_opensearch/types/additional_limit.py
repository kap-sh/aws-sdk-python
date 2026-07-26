"""Generated from Smithy shape ``com.amazonaws.opensearch#AdditionalLimit``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.limit_name
    import capo_opensearch.types.limit_value_list


class AdditionalLimit(TypedDict, closed=True):
    limit_name: NotRequired["capo_opensearch.types.limit_name.LimitName"]
    """<ul> <li> <p> <code>MaximumNumberOfDataNodesSupported</code> - This attribute only applies to master nodes and specifies the maximum number of data nodes of a given instance type a master node can support.</p> </li> <li> <p> <code>MaximumNumberOfDataNodesWithoutMasterNode</code> - This attribute only applies to data nodes and specifies the maximum number of data nodes of a given instance type can exist without a master node governing them.</p> </li> </ul>"""
    limit_values: NotRequired["capo_opensearch.types.limit_value_list.LimitValueList"]
    """<p> The values of the additional instance type limits.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdditionalLimit) -> dict:
    out: dict = {}
    if "limit_name" in value:
        out["LimitName"] = value["limit_name"]
    if "limit_values" in value:
        import capo_opensearch.types.limit_value_list

        out["LimitValues"] = capo_opensearch.types.limit_value_list.serialize_json(
            value["limit_values"]
        )
    return out


def deserialize_json(data: dict) -> AdditionalLimit:
    out: AdditionalLimit = {}  # type: ignore[typeddict-item]
    if "LimitName" in data:
        out["limit_name"] = data["LimitName"]
    if "LimitValues" in data:
        import capo_opensearch.types.limit_value_list

        out["limit_values"] = capo_opensearch.types.limit_value_list.deserialize_json(
            data["LimitValues"]
        )
    return out
