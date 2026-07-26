"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#StateTemplateAssociations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotfleetwise.types.state_template_association

StateTemplateAssociations: TypeAlias = list[
    "capo_iotfleetwise.types.state_template_association.StateTemplateAssociation"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StateTemplateAssociations) -> list:
    import capo_iotfleetwise.types.state_template_association

    out: list = []
    for item in value:
        out.append(
            capo_iotfleetwise.types.state_template_association.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> StateTemplateAssociations:
    import capo_iotfleetwise.types.state_template_association

    out: StateTemplateAssociations = []
    for item in data:
        out.append(
            capo_iotfleetwise.types.state_template_association.deserialize_aws_json_1_0(
                item
            )
        )
    return out
