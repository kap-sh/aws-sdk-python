"""Generated from Smithy shape ``com.amazonaws.glue#Blueprints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.blueprint

Blueprints: TypeAlias = list["capo_glue.types.blueprint.Blueprint"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Blueprints) -> list:
    import capo_glue.types.blueprint

    out: list = []
    for item in value:
        out.append(capo_glue.types.blueprint.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Blueprints:
    import capo_glue.types.blueprint

    out: Blueprints = []
    for item in data:
        out.append(capo_glue.types.blueprint.deserialize_aws_json_1_1(item))
    return out
