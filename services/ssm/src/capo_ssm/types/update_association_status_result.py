"""Generated from Smithy shape ``com.amazonaws.ssm#UpdateAssociationStatusResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.association_description


class UpdateAssociationStatusResult(TypedDict, closed=True):
    association_description: NotRequired[
        "capo_ssm.types.association_description.AssociationDescription"
    ]
    """<p>Information about the association.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateAssociationStatusResult) -> dict:
    out: dict = {}
    if "association_description" in value:
        import capo_ssm.types.association_description

        out["AssociationDescription"] = (
            capo_ssm.types.association_description.serialize_aws_json_1_1(
                value["association_description"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateAssociationStatusResult:
    out: UpdateAssociationStatusResult = {}  # type: ignore[typeddict-item]
    if "AssociationDescription" in data:
        import capo_ssm.types.association_description

        out["association_description"] = (
            capo_ssm.types.association_description.deserialize_aws_json_1_1(
                data["AssociationDescription"]
            )
        )
    return out
