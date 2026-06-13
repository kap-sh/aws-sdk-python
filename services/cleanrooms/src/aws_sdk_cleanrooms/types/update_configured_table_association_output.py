"""Generated from Smithy shape ``com.amazonaws.cleanrooms#UpdateConfiguredTableAssociationOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.configured_table_association


class UpdateConfiguredTableAssociationOutput(TypedDict):
    configured_table_association: "aws_sdk_cleanrooms.types.configured_table_association.ConfiguredTableAssociation"
    """<p>The entire updated configured table association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConfiguredTableAssociationOutput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.configured_table_association

    out["configuredTableAssociation"] = (
        aws_sdk_cleanrooms.types.configured_table_association.serialize_json(
            value["configured_table_association"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateConfiguredTableAssociationOutput:
    out: UpdateConfiguredTableAssociationOutput = {}  # type: ignore[typeddict-item]
    if "configuredTableAssociation" in data:
        import aws_sdk_cleanrooms.types.configured_table_association

        out["configured_table_association"] = (
            aws_sdk_cleanrooms.types.configured_table_association.deserialize_json(
                data["configuredTableAssociation"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateConfiguredTableAssociationOutput.configured_table_association required"
        )
    return out
