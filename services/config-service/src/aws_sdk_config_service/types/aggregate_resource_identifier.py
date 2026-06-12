"""Generated from Smithy shape ``com.amazonaws.configservice#AggregateResourceIdentifier``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.account_id
    import aws_sdk_config_service.types.aws_region
    import aws_sdk_config_service.types.resource_id
    import aws_sdk_config_service.types.resource_name
    import aws_sdk_config_service.types.resource_type


class AggregateResourceIdentifier(TypedDict):
    source_account_id: "aws_sdk_config_service.types.account_id.AccountId"
    """<p>The 12-digit account ID of the source account.</p>"""
    source_region: "aws_sdk_config_service.types.aws_region.AwsRegion"
    """<p>The source region where data is aggregated.</p>"""
    resource_id: "aws_sdk_config_service.types.resource_id.ResourceId"
    """<p>The ID of the Amazon Web Services resource.</p>"""
    resource_type: "aws_sdk_config_service.types.resource_type.ResourceType"
    """<p>The type of the Amazon Web Services resource.</p>"""
    resource_name: NotRequired[
        "aws_sdk_config_service.types.resource_name.ResourceName"
    ]
    """<p>The name of the Amazon Web Services resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggregateResourceIdentifier) -> dict:
    out: dict = {}
    out["SourceAccountId"] = value["source_account_id"]
    out["SourceRegion"] = value["source_region"]
    out["ResourceId"] = value["resource_id"]
    import aws_sdk_config_service.types.resource_type

    out["ResourceType"] = (
        aws_sdk_config_service.types.resource_type.serialize_aws_json_1_1(
            value["resource_type"]
        )
    )
    if "resource_name" in value:
        out["ResourceName"] = value["resource_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AggregateResourceIdentifier:
    out: AggregateResourceIdentifier = {}  # type: ignore[typeddict-item]
    if "SourceAccountId" in data:
        out["source_account_id"] = data["SourceAccountId"]
    else:
        raise DeserializationError(
            "AggregateResourceIdentifier.source_account_id required"
        )
    if "SourceRegion" in data:
        out["source_region"] = data["SourceRegion"]
    else:
        raise DeserializationError("AggregateResourceIdentifier.source_region required")
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("AggregateResourceIdentifier.resource_id required")
    if "ResourceType" in data:
        import aws_sdk_config_service.types.resource_type

        out["resource_type"] = (
            aws_sdk_config_service.types.resource_type.deserialize_aws_json_1_1(
                data["ResourceType"]
            )
        )
    else:
        raise DeserializationError("AggregateResourceIdentifier.resource_type required")
    if "ResourceName" in data:
        out["resource_name"] = data["ResourceName"]
    return out
