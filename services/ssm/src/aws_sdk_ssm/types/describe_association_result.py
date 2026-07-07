"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeAssociationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.association_description


class DescribeAssociationResult(TypedDict, closed=True):
    association_description: NotRequired[
        "aws_sdk_ssm.types.association_description.AssociationDescription"
    ]
    """<p>Information about the association.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAssociationResult) -> dict:
    out: dict = {}
    if "association_description" in value:
        import aws_sdk_ssm.types.association_description

        out["AssociationDescription"] = (
            aws_sdk_ssm.types.association_description.serialize_aws_json_1_1(
                value["association_description"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAssociationResult:
    out: DescribeAssociationResult = {}  # type: ignore[typeddict-item]
    if "AssociationDescription" in data:
        import aws_sdk_ssm.types.association_description

        out["association_description"] = (
            aws_sdk_ssm.types.association_description.deserialize_aws_json_1_1(
                data["AssociationDescription"]
            )
        )
    return out
