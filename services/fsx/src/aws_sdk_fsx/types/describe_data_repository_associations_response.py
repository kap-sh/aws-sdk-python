"""Generated from Smithy shape ``com.amazonaws.fsx#DescribeDataRepositoryAssociationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.data_repository_associations
    import aws_sdk_fsx.types.next_token


class DescribeDataRepositoryAssociationsResponse(TypedDict):
    associations: NotRequired[
        "aws_sdk_fsx.types.data_repository_associations.DataRepositoryAssociations"
    ]
    """<p>An array of one or more data repository association descriptions.</p>"""
    next_token: NotRequired["aws_sdk_fsx.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDataRepositoryAssociationsResponse) -> dict:
    out: dict = {}
    if "associations" in value:
        import aws_sdk_fsx.types.data_repository_associations

        out["Associations"] = (
            aws_sdk_fsx.types.data_repository_associations.serialize_aws_json_1_1(
                value["associations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDataRepositoryAssociationsResponse:
    out: DescribeDataRepositoryAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "Associations" in data:
        import aws_sdk_fsx.types.data_repository_associations

        out["associations"] = (
            aws_sdk_fsx.types.data_repository_associations.deserialize_aws_json_1_1(
                data["Associations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
