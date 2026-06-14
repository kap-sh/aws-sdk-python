"""Generated from Smithy shape ``com.amazonaws.storagegateway#DescribeTapesInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.gateway_arn
    import aws_sdk_storage_gateway.types.marker
    import aws_sdk_storage_gateway.types.positive_int_object
    import aws_sdk_storage_gateway.types.tape_ar_ns


class DescribeTapesInput(TypedDict):
    gateway_arn: "aws_sdk_storage_gateway.types.gateway_arn.GatewayARN"
    tape_ar_ns: NotRequired["aws_sdk_storage_gateway.types.tape_ar_ns.TapeARNs"]
    """<p>Specifies one or more unique Amazon Resource Names (ARNs) that represent the virtual tapes you want to describe. If this parameter is not specified, Tape gateway returns a description of all virtual tapes associated with the specified gateway.</p>"""
    marker: NotRequired["aws_sdk_storage_gateway.types.marker.Marker"]
    """<p>A marker value, obtained in a previous call to <code>DescribeTapes</code>. This marker indicates which page of results to retrieve.</p> <p>If not specified, the first page of results is retrieved.</p>"""
    limit: NotRequired[
        "aws_sdk_storage_gateway.types.positive_int_object.PositiveIntObject"
    ]
    """<p>Specifies that the number of virtual tapes described be limited to the specified number.</p> <note> <p>Amazon Web Services may impose its own limit, if this field is not set.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTapesInput) -> dict:
    out: dict = {}
    out["GatewayARN"] = value["gateway_arn"]
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


def deserialize_aws_json_1_1(data: dict) -> DescribeTapesInput:
    out: DescribeTapesInput = {}  # type: ignore[typeddict-item]
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    else:
        raise DeserializationError("DescribeTapesInput.gateway_arn required")
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
