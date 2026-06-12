"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#DescribeConfigurationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_application_discovery_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.configuration_id_list


class DescribeConfigurationsRequest(TypedDict):
    configuration_ids: "aws_sdk_application_discovery_service.types.configuration_id_list.ConfigurationIdList"
    """<p>One or more configuration IDs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConfigurationsRequest) -> dict:
    out: dict = {}
    import aws_sdk_application_discovery_service.types.configuration_id_list

    out["configurationIds"] = (
        aws_sdk_application_discovery_service.types.configuration_id_list.serialize_aws_json_1_1(
            value["configuration_ids"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConfigurationsRequest:
    out: DescribeConfigurationsRequest = {}  # type: ignore[typeddict-item]
    if "configurationIds" in data:
        import aws_sdk_application_discovery_service.types.configuration_id_list

        out["configuration_ids"] = (
            aws_sdk_application_discovery_service.types.configuration_id_list.deserialize_aws_json_1_1(
                data["configurationIds"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeConfigurationsRequest.configuration_ids required"
        )
    return out
