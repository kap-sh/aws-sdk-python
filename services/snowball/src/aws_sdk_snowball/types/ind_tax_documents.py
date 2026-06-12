"""Generated from Smithy shape ``com.amazonaws.snowball#INDTaxDocuments``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_snowball.types.gstin


class INDTaxDocuments(TypedDict):
    gstin: NotRequired["aws_sdk_snowball.types.gstin.GSTIN"]
    """<p>The Goods and Services Tax (GST) documents required in Amazon Web Services Region in India.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: INDTaxDocuments) -> dict:
    out: dict = {}
    if "gstin" in value:
        out["GSTIN"] = value["gstin"]
    return out


def deserialize_aws_json_1_1(data: dict) -> INDTaxDocuments:
    out: INDTaxDocuments = {}  # type: ignore[typeddict-item]
    if "GSTIN" in data:
        out["gstin"] = data["GSTIN"]
    return out
