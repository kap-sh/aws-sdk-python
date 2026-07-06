"""Generated from Smithy shape ``com.amazonaws.snowball#TaxDocuments``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_snowball.types.ind_tax_documents


class TaxDocuments(TypedDict, closed=True):
    ind: NotRequired["aws_sdk_snowball.types.ind_tax_documents.INDTaxDocuments"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaxDocuments) -> dict:
    out: dict = {}
    if "ind" in value:
        import aws_sdk_snowball.types.ind_tax_documents

        out["IND"] = aws_sdk_snowball.types.ind_tax_documents.serialize_aws_json_1_1(
            value["ind"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TaxDocuments:
    out: TaxDocuments = {}  # type: ignore[typeddict-item]
    if "IND" in data:
        import aws_sdk_snowball.types.ind_tax_documents

        out["ind"] = aws_sdk_snowball.types.ind_tax_documents.deserialize_aws_json_1_1(
            data["IND"]
        )
    return out
