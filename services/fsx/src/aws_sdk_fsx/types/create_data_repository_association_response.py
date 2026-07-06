"""Generated from Smithy shape ``com.amazonaws.fsx#CreateDataRepositoryAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.data_repository_association


class CreateDataRepositoryAssociationResponse(TypedDict, closed=True):
    association: NotRequired[
        "aws_sdk_fsx.types.data_repository_association.DataRepositoryAssociation"
    ]
    """<p>The response object returned after the data repository association is created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDataRepositoryAssociationResponse) -> dict:
    out: dict = {}
    if "association" in value:
        import aws_sdk_fsx.types.data_repository_association

        out["Association"] = (
            aws_sdk_fsx.types.data_repository_association.serialize_aws_json_1_1(
                value["association"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDataRepositoryAssociationResponse:
    out: CreateDataRepositoryAssociationResponse = {}  # type: ignore[typeddict-item]
    if "Association" in data:
        import aws_sdk_fsx.types.data_repository_association

        out["association"] = (
            aws_sdk_fsx.types.data_repository_association.deserialize_aws_json_1_1(
                data["Association"]
            )
        )
    return out
