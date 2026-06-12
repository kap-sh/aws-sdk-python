"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#AdditionalLimit``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.limit_name
    import aws_sdk_elasticsearch_service.types.limit_value_list


class AdditionalLimit(TypedDict):
    limit_name: NotRequired["aws_sdk_elasticsearch_service.types.limit_name.LimitName"]
    """<p> Name of Additional Limit is specific to a given InstanceType and for each of it's <code> <a>InstanceRole</a> </code> etc. <br></br> Attributes and their details: <br></br> <ul> <li>MaximumNumberOfDataNodesSupported</li> This attribute will be present in Master node only to specify how much data nodes upto which given <code> <a>ESPartitionInstanceType</a> </code> can support as master node. <li>MaximumNumberOfDataNodesWithoutMasterNode</li> This attribute will be present in Data node only to specify how much data nodes of given <code> <a>ESPartitionInstanceType</a> </code> upto which you don't need any master nodes to govern them. </ul> </p>"""
    limit_values: NotRequired[
        "aws_sdk_elasticsearch_service.types.limit_value_list.LimitValueList"
    ]
    """<p> Value for given <code> <a>AdditionalLimit$LimitName</a> </code> . </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdditionalLimit) -> dict:
    out: dict = {}
    if "limit_name" in value:
        out["LimitName"] = value["limit_name"]
    if "limit_values" in value:
        import aws_sdk_elasticsearch_service.types.limit_value_list

        out["LimitValues"] = (
            aws_sdk_elasticsearch_service.types.limit_value_list.serialize_json(
                value["limit_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> AdditionalLimit:
    out: AdditionalLimit = {}  # type: ignore[typeddict-item]
    if "LimitName" in data:
        out["limit_name"] = data["LimitName"]
    if "LimitValues" in data:
        import aws_sdk_elasticsearch_service.types.limit_value_list

        out["limit_values"] = (
            aws_sdk_elasticsearch_service.types.limit_value_list.deserialize_json(
                data["LimitValues"]
            )
        )
    return out
