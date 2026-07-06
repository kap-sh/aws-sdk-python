"""Generated from Smithy shape ``com.amazonaws.b2bi#X12Details``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.x12_transaction_set
    import aws_sdk_b2bi.types.x12_version


class X12Details(TypedDict, closed=True):
    transaction_set: NotRequired[
        "aws_sdk_b2bi.types.x12_transaction_set.X12TransactionSet"
    ]
    """<p>Returns an enumerated type where each value identifies an X12 transaction set. Transaction sets are maintained by the X12 Accredited Standards Committee.</p>"""
    version: NotRequired["aws_sdk_b2bi.types.x12_version.X12Version"]
    """<p>Returns the version to use for the specified X12 transaction set.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: X12Details) -> dict:
    out: dict = {}
    if "transaction_set" in value:
        import aws_sdk_b2bi.types.x12_transaction_set

        out["transactionSet"] = (
            aws_sdk_b2bi.types.x12_transaction_set.serialize_aws_json_1_0(
                value["transaction_set"]
            )
        )
    if "version" in value:
        import aws_sdk_b2bi.types.x12_version

        out["version"] = aws_sdk_b2bi.types.x12_version.serialize_aws_json_1_0(
            value["version"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> X12Details:
    out: X12Details = {}  # type: ignore[typeddict-item]
    if "transactionSet" in data:
        import aws_sdk_b2bi.types.x12_transaction_set

        out["transaction_set"] = (
            aws_sdk_b2bi.types.x12_transaction_set.deserialize_aws_json_1_0(
                data["transactionSet"]
            )
        )
    if "version" in data:
        import aws_sdk_b2bi.types.x12_version

        out["version"] = aws_sdk_b2bi.types.x12_version.deserialize_aws_json_1_0(
            data["version"]
        )
    return out
