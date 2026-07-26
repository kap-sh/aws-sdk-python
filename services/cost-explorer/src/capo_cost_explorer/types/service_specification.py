"""Generated from Smithy shape ``com.amazonaws.costexplorer#ServiceSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.ec2_specification


class ServiceSpecification(TypedDict, closed=True):
    ec2_specification: NotRequired[
        "capo_cost_explorer.types.ec2_specification.EC2Specification"
    ]
    """<p>The Amazon EC2 hardware specifications that you want Amazon Web Services to provide recommendations for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceSpecification) -> dict:
    out: dict = {}
    if "ec2_specification" in value:
        import capo_cost_explorer.types.ec2_specification

        out["EC2Specification"] = (
            capo_cost_explorer.types.ec2_specification.serialize_aws_json_1_1(
                value["ec2_specification"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceSpecification:
    out: ServiceSpecification = {}  # type: ignore[typeddict-item]
    if "EC2Specification" in data:
        import capo_cost_explorer.types.ec2_specification

        out["ec2_specification"] = (
            capo_cost_explorer.types.ec2_specification.deserialize_aws_json_1_1(
                data["EC2Specification"]
            )
        )
    return out
