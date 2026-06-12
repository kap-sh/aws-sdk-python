"""Generated from Smithy shape ``com.amazonaws.costexplorer#ServiceSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.ec2_specification


class ServiceSpecification(TypedDict):
    ec2_specification: NotRequired[
        "aws_sdk_cost_explorer.types.ec2_specification.EC2Specification"
    ]
    """<p>The Amazon EC2 hardware specifications that you want Amazon Web Services to provide recommendations for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceSpecification) -> dict:
    out: dict = {}
    if "ec2_specification" in value:
        import aws_sdk_cost_explorer.types.ec2_specification

        out["EC2Specification"] = (
            aws_sdk_cost_explorer.types.ec2_specification.serialize_aws_json_1_1(
                value["ec2_specification"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceSpecification:
    out: ServiceSpecification = {}  # type: ignore[typeddict-item]
    if "EC2Specification" in data:
        import aws_sdk_cost_explorer.types.ec2_specification

        out["ec2_specification"] = (
            aws_sdk_cost_explorer.types.ec2_specification.deserialize_aws_json_1_1(
                data["EC2Specification"]
            )
        )
    return out
