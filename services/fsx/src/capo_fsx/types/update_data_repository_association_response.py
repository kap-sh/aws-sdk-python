"""Generated from Smithy shape ``com.amazonaws.fsx#UpdateDataRepositoryAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.data_repository_association


class UpdateDataRepositoryAssociationResponse(TypedDict, closed=True):
    association: NotRequired[
        "capo_fsx.types.data_repository_association.DataRepositoryAssociation"
    ]
    """<p>The response object returned after the data repository association is updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDataRepositoryAssociationResponse) -> dict:
    out: dict = {}
    if "association" in value:
        import capo_fsx.types.data_repository_association

        out["Association"] = (
            capo_fsx.types.data_repository_association.serialize_aws_json_1_1(
                value["association"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDataRepositoryAssociationResponse:
    out: UpdateDataRepositoryAssociationResponse = {}  # type: ignore[typeddict-item]
    if "Association" in data:
        import capo_fsx.types.data_repository_association

        out["association"] = (
            capo_fsx.types.data_repository_association.deserialize_aws_json_1_1(
                data["Association"]
            )
        )
    return out
