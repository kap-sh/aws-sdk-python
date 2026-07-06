"""Generated from Smithy shape ``com.amazonaws.configservice#AssociateResourceTypesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.amazon_resource_name
    import aws_sdk_config_service.types.resource_type_list


class AssociateResourceTypesRequest(TypedDict, closed=True):
    configuration_recorder_arn: (
        "aws_sdk_config_service.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>The Amazon Resource Name (ARN) of the specified configuration recorder.</p>"""
    resource_types: "aws_sdk_config_service.types.resource_type_list.ResourceTypeList"
    """<p>The list of resource types you want to add to the recording group of the specified configuration recorder.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateResourceTypesRequest) -> dict:
    out: dict = {}
    out["ConfigurationRecorderArn"] = value["configuration_recorder_arn"]
    import aws_sdk_config_service.types.resource_type_list

    out["ResourceTypes"] = (
        aws_sdk_config_service.types.resource_type_list.serialize_aws_json_1_1(
            value["resource_types"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateResourceTypesRequest:
    out: AssociateResourceTypesRequest = {}  # type: ignore[typeddict-item]
    if "ConfigurationRecorderArn" in data:
        out["configuration_recorder_arn"] = data["ConfigurationRecorderArn"]
    else:
        raise DeserializationError(
            "AssociateResourceTypesRequest.configuration_recorder_arn required"
        )
    if "ResourceTypes" in data:
        import aws_sdk_config_service.types.resource_type_list

        out["resource_types"] = (
            aws_sdk_config_service.types.resource_type_list.deserialize_aws_json_1_1(
                data["ResourceTypes"]
            )
        )
    else:
        raise DeserializationError(
            "AssociateResourceTypesRequest.resource_types required"
        )
    return out
