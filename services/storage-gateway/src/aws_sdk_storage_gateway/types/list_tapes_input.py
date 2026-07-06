"""Generated from Smithy shape ``com.amazonaws.storagegateway#ListTapesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.marker
    import aws_sdk_storage_gateway.types.positive_int_object
    import aws_sdk_storage_gateway.types.tape_ar_ns


class ListTapesInput(TypedDict, closed=True):
    tape_ar_ns: NotRequired["aws_sdk_storage_gateway.types.tape_ar_ns.TapeARNs"]
    marker: NotRequired["aws_sdk_storage_gateway.types.marker.Marker"]
    """<p>A string that indicates the position at which to begin the returned list of tapes.</p>"""
    limit: NotRequired[
        "aws_sdk_storage_gateway.types.positive_int_object.PositiveIntObject"
    ]
    """<p>An optional number limit for the tapes in the list returned by this call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTapesInput) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> ListTapesInput:
    out: ListTapesInput = {}  # type: ignore[typeddict-item]
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
