"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#GetMpaTeamAssociationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import capo_payment_cryptography.types.mpa_team_association


class GetMpaTeamAssociationOutput(TypedDict, closed=True):
    mpa_team_association: (
        "capo_payment_cryptography.types.mpa_team_association.MpaTeamAssociation"
    )
    """<p>The details of the MPA team association.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetMpaTeamAssociationOutput) -> dict:
    out: dict = {}
    import capo_payment_cryptography.types.mpa_team_association

    out["MpaTeamAssociation"] = (
        capo_payment_cryptography.types.mpa_team_association.serialize_aws_json_1_0(
            value["mpa_team_association"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetMpaTeamAssociationOutput:
    out: GetMpaTeamAssociationOutput = {}  # type: ignore[typeddict-item]
    if "MpaTeamAssociation" in data:
        import capo_payment_cryptography.types.mpa_team_association

        out["mpa_team_association"] = (
            capo_payment_cryptography.types.mpa_team_association.deserialize_aws_json_1_0(
                data["MpaTeamAssociation"]
            )
        )
    else:
        raise DeserializationError(
            "GetMpaTeamAssociationOutput.mpa_team_association required"
        )
    return out
