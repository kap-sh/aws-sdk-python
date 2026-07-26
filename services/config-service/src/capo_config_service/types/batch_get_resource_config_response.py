"""Generated from Smithy shape ``com.amazonaws.configservice#BatchGetResourceConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.base_configuration_items
    import capo_config_service.types.resource_keys


class BatchGetResourceConfigResponse(TypedDict, closed=True):
    base_configuration_items: NotRequired[
        "capo_config_service.types.base_configuration_items.BaseConfigurationItems"
    ]
    """<p>A list that contains the current configuration of one or more resources.</p>"""
    unprocessed_resource_keys: NotRequired[
        "capo_config_service.types.resource_keys.ResourceKeys"
    ]
    """<p>A list of resource keys that were not processed with the current response. The unprocessesResourceKeys value is in the same form as ResourceKeys, so the value can be directly provided to a subsequent BatchGetResourceConfig operation. If there are no unprocessed resource keys, the response contains an empty unprocessedResourceKeys list. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetResourceConfigResponse) -> dict:
    out: dict = {}
    if "base_configuration_items" in value:
        import capo_config_service.types.base_configuration_items

        out["baseConfigurationItems"] = (
            capo_config_service.types.base_configuration_items.serialize_aws_json_1_1(
                value["base_configuration_items"]
            )
        )
    if "unprocessed_resource_keys" in value:
        import capo_config_service.types.resource_keys

        out["unprocessedResourceKeys"] = (
            capo_config_service.types.resource_keys.serialize_aws_json_1_1(
                value["unprocessed_resource_keys"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetResourceConfigResponse:
    out: BatchGetResourceConfigResponse = {}  # type: ignore[typeddict-item]
    if "baseConfigurationItems" in data:
        import capo_config_service.types.base_configuration_items

        out["base_configuration_items"] = (
            capo_config_service.types.base_configuration_items.deserialize_aws_json_1_1(
                data["baseConfigurationItems"]
            )
        )
    if "unprocessedResourceKeys" in data:
        import capo_config_service.types.resource_keys

        out["unprocessed_resource_keys"] = (
            capo_config_service.types.resource_keys.deserialize_aws_json_1_1(
                data["unprocessedResourceKeys"]
            )
        )
    return out
