"""Generated from Smithy shape ``com.amazonaws.proton#ListServiceInstancesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.next_token
    import aws_sdk_proton.types.service_instance_summary_list


class ListServiceInstancesOutput(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_proton.types.next_token.NextToken"]
    """<p>A token that indicates the location of the next service instance in the array of service instances, after the current requested list of service instances.</p>"""
    service_instances: (
        "aws_sdk_proton.types.service_instance_summary_list.ServiceInstanceSummaryList"
    )
    """<p>An array of service instances with summary data.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListServiceInstancesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_proton.types.service_instance_summary_list

    out["serviceInstances"] = (
        aws_sdk_proton.types.service_instance_summary_list.serialize_aws_json_1_0(
            value["service_instances"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListServiceInstancesOutput:
    out: ListServiceInstancesOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "serviceInstances" in data:
        import aws_sdk_proton.types.service_instance_summary_list

        out["service_instances"] = (
            aws_sdk_proton.types.service_instance_summary_list.deserialize_aws_json_1_0(
                data["serviceInstances"]
            )
        )
    else:
        raise DeserializationError(
            "ListServiceInstancesOutput.service_instances required"
        )
    return out
