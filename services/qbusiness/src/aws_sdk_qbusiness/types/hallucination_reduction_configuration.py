"""Generated from Smithy shape ``com.amazonaws.qbusiness#HallucinationReductionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.hallucination_reduction_control


class HallucinationReductionConfiguration(TypedDict):
    hallucination_reduction_control: NotRequired[
        "aws_sdk_qbusiness.types.hallucination_reduction_control.HallucinationReductionControl"
    ]
    """<p>Controls whether hallucination reduction has been enabled or disabled for your application. The default status is <code>DISABLED</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HallucinationReductionConfiguration) -> dict:
    out: dict = {}
    if "hallucination_reduction_control" in value:
        import aws_sdk_qbusiness.types.hallucination_reduction_control

        out["hallucinationReductionControl"] = (
            aws_sdk_qbusiness.types.hallucination_reduction_control.serialize_json(
                value["hallucination_reduction_control"]
            )
        )
    return out


def deserialize_json(data: dict) -> HallucinationReductionConfiguration:
    out: HallucinationReductionConfiguration = {}  # type: ignore[typeddict-item]
    if "hallucinationReductionControl" in data:
        import aws_sdk_qbusiness.types.hallucination_reduction_control

        out["hallucination_reduction_control"] = (
            aws_sdk_qbusiness.types.hallucination_reduction_control.deserialize_json(
                data["hallucinationReductionControl"]
            )
        )
    return out
