"""Generated from Smithy shape ``com.amazonaws.glue#ModifyIntegrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.integration_config
    import aws_sdk_glue.types.integration_description
    import aws_sdk_glue.types.string128
    import aws_sdk_glue.types.string2048


class ModifyIntegrationRequest(TypedDict, closed=True):
    integration_identifier: "aws_sdk_glue.types.string128.String128"
    """<p>The Amazon Resource Name (ARN) for the integration.</p>"""
    description: NotRequired[
        "aws_sdk_glue.types.integration_description.IntegrationDescription"
    ]
    """<p>A description of the integration.</p>"""
    data_filter: NotRequired["aws_sdk_glue.types.string2048.String2048"]
    """<p>Selects source tables for the integration using Maxwell filter syntax.</p>"""
    integration_config: NotRequired[
        "aws_sdk_glue.types.integration_config.IntegrationConfig"
    ]
    """<p>The configuration settings for the integration. Currently, only the RefreshInterval can be modified. </p>"""
    integration_name: NotRequired["aws_sdk_glue.types.string128.String128"]
    """<p>A unique name for an integration in Glue.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyIntegrationRequest) -> dict:
    out: dict = {}
    out["IntegrationIdentifier"] = value["integration_identifier"]
    if "description" in value:
        out["Description"] = value["description"]
    if "data_filter" in value:
        out["DataFilter"] = value["data_filter"]
    if "integration_config" in value:
        import aws_sdk_glue.types.integration_config

        out["IntegrationConfig"] = (
            aws_sdk_glue.types.integration_config.serialize_aws_json_1_1(
                value["integration_config"]
            )
        )
    if "integration_name" in value:
        out["IntegrationName"] = value["integration_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyIntegrationRequest:
    out: ModifyIntegrationRequest = {}  # type: ignore[typeddict-item]
    if "IntegrationIdentifier" in data:
        out["integration_identifier"] = data["IntegrationIdentifier"]
    else:
        raise DeserializationError(
            "ModifyIntegrationRequest.integration_identifier required"
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "DataFilter" in data:
        out["data_filter"] = data["DataFilter"]
    if "IntegrationConfig" in data:
        import aws_sdk_glue.types.integration_config

        out["integration_config"] = (
            aws_sdk_glue.types.integration_config.deserialize_aws_json_1_1(
                data["IntegrationConfig"]
            )
        )
    if "IntegrationName" in data:
        out["integration_name"] = data["IntegrationName"]
    return out
