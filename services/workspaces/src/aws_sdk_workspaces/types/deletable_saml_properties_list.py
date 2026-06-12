"""Generated from Smithy shape ``com.amazonaws.workspaces#DeletableSamlPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.deletable_saml_property

DeletableSamlPropertiesList: TypeAlias = list[
    "aws_sdk_workspaces.types.deletable_saml_property.DeletableSamlProperty"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletableSamlPropertiesList) -> list:
    import aws_sdk_workspaces.types.deletable_saml_property

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces.types.deletable_saml_property.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DeletableSamlPropertiesList:
    import aws_sdk_workspaces.types.deletable_saml_property

    out: DeletableSamlPropertiesList = []
    for item in data:
        out.append(
            aws_sdk_workspaces.types.deletable_saml_property.deserialize_aws_json_1_1(
                item
            )
        )
    return out
