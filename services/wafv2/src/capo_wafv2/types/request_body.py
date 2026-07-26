"""Generated from Smithy shape ``com.amazonaws.wafv2#RequestBody``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.associated_resource_type
    import capo_wafv2.types.request_body_associated_resource_type_config

RequestBody: TypeAlias = dict[
    "capo_wafv2.types.associated_resource_type.AssociatedResourceType",
    "capo_wafv2.types.request_body_associated_resource_type_config.RequestBodyAssociatedResourceTypeConfig",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: RequestBody) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_wafv2.types.associated_resource_type
        import capo_wafv2.types.request_body_associated_resource_type_config

        out[capo_wafv2.types.associated_resource_type.serialize_aws_json_1_1(key)] = (
            capo_wafv2.types.request_body_associated_resource_type_config.serialize_aws_json_1_1(
                value
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RequestBody:
    out: RequestBody = {}
    for key, value in data.items():
        import capo_wafv2.types.associated_resource_type
        import capo_wafv2.types.request_body_associated_resource_type_config

        out[capo_wafv2.types.associated_resource_type.deserialize_aws_json_1_1(key)] = (
            capo_wafv2.types.request_body_associated_resource_type_config.deserialize_aws_json_1_1(
                value
            )
        )
    return out
