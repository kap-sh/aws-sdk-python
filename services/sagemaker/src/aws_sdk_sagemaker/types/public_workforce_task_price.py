"""Generated from Smithy shape ``com.amazonaws.sagemaker#PublicWorkforceTaskPrice``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.usd


class PublicWorkforceTaskPrice(TypedDict, closed=True):
    amount_in_usd: NotRequired["aws_sdk_sagemaker.types.usd.USD"]
    """<p>Defines the amount of money paid to an Amazon Mechanical Turk worker in United States dollars.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PublicWorkforceTaskPrice) -> dict:
    out: dict = {}
    if "amount_in_usd" in value:
        import aws_sdk_sagemaker.types.usd

        out["AmountInUsd"] = aws_sdk_sagemaker.types.usd.serialize_aws_json_1_1(
            value["amount_in_usd"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PublicWorkforceTaskPrice:
    out: PublicWorkforceTaskPrice = {}  # type: ignore[typeddict-item]
    if "AmountInUsd" in data:
        import aws_sdk_sagemaker.types.usd

        out["amount_in_usd"] = aws_sdk_sagemaker.types.usd.deserialize_aws_json_1_1(
            data["AmountInUsd"]
        )
    return out
