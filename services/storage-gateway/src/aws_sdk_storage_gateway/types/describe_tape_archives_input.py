"""Generated from Smithy shape ``com.amazonaws.storagegateway#DescribeTapeArchivesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.marker
    import aws_sdk_storage_gateway.types.positive_int_object
    import aws_sdk_storage_gateway.types.tape_ar_ns


class DescribeTapeArchivesInput(TypedDict, closed=True):
    tape_ar_ns: NotRequired["aws_sdk_storage_gateway.types.tape_ar_ns.TapeARNs"]
    """<p>Specifies one or more unique Amazon Resource Names (ARNs) that represent the virtual tapes you want to describe.</p>"""
    marker: NotRequired["aws_sdk_storage_gateway.types.marker.Marker"]
    """<p>An opaque string that indicates the position at which to begin describing virtual tapes.</p>"""
    limit: NotRequired[
        "aws_sdk_storage_gateway.types.positive_int_object.PositiveIntObject"
    ]
    """<p>Specifies that the number of virtual tapes described be limited to the specified number.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTapeArchivesInput) -> dict:
    out: dict = {}
    if "tape_ar_ns" in value:
        import aws_sdk_storage_gateway.types.tape_ar_ns

        out["TapeARNs"] = (
            aws_sdk_storage_gateway.types.tape_ar_ns.serialize_aws_json_1_1(
                value["tape_ar_ns"]
            )
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTapeArchivesInput:
    out: DescribeTapeArchivesInput = {}  # type: ignore[typeddict-item]
    if "TapeARNs" in data:
        import aws_sdk_storage_gateway.types.tape_ar_ns

        out["tape_ar_ns"] = (
            aws_sdk_storage_gateway.types.tape_ar_ns.deserialize_aws_json_1_1(
                data["TapeARNs"]
            )
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    return out
