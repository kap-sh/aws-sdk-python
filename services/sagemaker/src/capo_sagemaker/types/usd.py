"""Generated from Smithy shape ``com.amazonaws.sagemaker#USD``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cents
    import capo_sagemaker.types.dollars
    import capo_sagemaker.types.tenth_fractions_of_a_cent


class USD(TypedDict, closed=True):
    dollars: NotRequired["capo_sagemaker.types.dollars.Dollars"]
    """<p>The whole number of dollars in the amount.</p>"""
    cents: NotRequired["capo_sagemaker.types.cents.Cents"]
    """<p>The fractional portion, in cents, of the amount. </p>"""
    tenth_fractions_of_a_cent: NotRequired[
        "capo_sagemaker.types.tenth_fractions_of_a_cent.TenthFractionsOfACent"
    ]
    """<p>Fractions of a cent, in tenths.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: USD) -> dict:
    out: dict = {}
    if "dollars" in value:
        out["Dollars"] = value["dollars"]
    if "cents" in value:
        out["Cents"] = value["cents"]
    if "tenth_fractions_of_a_cent" in value:
        out["TenthFractionsOfACent"] = value["tenth_fractions_of_a_cent"]
    return out


def deserialize_aws_json_1_1(data: dict) -> USD:
    out: USD = {}  # type: ignore[typeddict-item]
    if "Dollars" in data:
        out["dollars"] = data["Dollars"]
    if "Cents" in data:
        out["cents"] = data["Cents"]
    if "TenthFractionsOfACent" in data:
        out["tenth_fractions_of_a_cent"] = data["TenthFractionsOfACent"]
    return out
