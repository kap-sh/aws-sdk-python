"""Generated from Smithy shape ``com.amazonaws.configservice#BatchGetAggregateResourceConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.base_configuration_items
    import aws_sdk_config_service.types.unprocessed_resource_identifier_list


class BatchGetAggregateResourceConfigResponse(TypedDict, closed=True):
    base_configuration_items: NotRequired[
        "aws_sdk_config_service.types.base_configuration_items.BaseConfigurationItems"
    ]
    """<p>A list that contains the current configuration of one or more resources.</p>"""
    unprocessed_resource_identifiers: NotRequired[
        "aws_sdk_config_service.types.unprocessed_resource_identifier_list.UnprocessedResourceIdentifierList"
    ]
    """<p>A list of resource identifiers that were not processed with current scope. The list is empty if all the resources are processed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetAggregateResourceConfigResponse) -> dict:
    out: dict = {}
    if "base_configuration_items" in value:
        import aws_sdk_config_service.types.base_configuration_items

        out["BaseConfigurationItems"] = (
            aws_sdk_config_service.types.base_configuration_items.serialize_aws_json_1_1(
                value["base_configuration_items"]
            )
        )
    if "unprocessed_resource_identifiers" in value:
        import aws_sdk_config_service.types.unprocessed_resource_identifier_list

        out["UnprocessedResourceIdentifiers"] = (
            aws_sdk_config_service.types.unprocessed_resource_identifier_list.serialize_aws_json_1_1(
                value["unprocessed_resource_identifiers"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetAggregateResourceConfigResponse:
    out: BatchGetAggregateResourceConfigResponse = {}  # type: ignore[typeddict-item]
    if "BaseConfigurationItems" in data:
        import aws_sdk_config_service.types.base_configuration_items

        out["base_configuration_items"] = (
            aws_sdk_config_service.types.base_configuration_items.deserialize_aws_json_1_1(
                data["BaseConfigurationItems"]
            )
        )
    if "UnprocessedResourceIdentifiers" in data:
        import aws_sdk_config_service.types.unprocessed_resource_identifier_list

        out["unprocessed_resource_identifiers"] = (
            aws_sdk_config_service.types.unprocessed_resource_identifier_list.deserialize_aws_json_1_1(
                data["UnprocessedResourceIdentifiers"]
            )
        )
    return out
