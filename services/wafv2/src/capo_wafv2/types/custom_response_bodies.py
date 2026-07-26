"""Generated from Smithy shape ``com.amazonaws.wafv2#CustomResponseBodies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.custom_response_body
    import capo_wafv2.types.entity_name

CustomResponseBodies: TypeAlias = dict[
    "capo_wafv2.types.entity_name.EntityName",
    "capo_wafv2.types.custom_response_body.CustomResponseBody",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: CustomResponseBodies) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_wafv2.types.custom_response_body

        out[key] = capo_wafv2.types.custom_response_body.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomResponseBodies:
    out: CustomResponseBodies = {}
    for key, value in data.items():
        import capo_wafv2.types.custom_response_body

        out[key] = capo_wafv2.types.custom_response_body.deserialize_aws_json_1_1(value)
    return out
