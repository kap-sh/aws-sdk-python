"""Generated from Smithy shape ``com.amazonaws.b2bi#TestConversionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_b2bi.errors import DeserializationError

if TYPE_CHECKING:
    import capo_b2bi.types.conversion_source
    import capo_b2bi.types.conversion_target


class TestConversionRequest(TypedDict, closed=True):
    source: "capo_b2bi.types.conversion_source.ConversionSource"
    """<p>Specify the source file for an outbound EDI request.</p>"""
    target: "capo_b2bi.types.conversion_target.ConversionTarget"
    """<p>Specify the format (X12 is the only currently supported format), and other details for the conversion target.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TestConversionRequest) -> dict:
    out: dict = {}
    import capo_b2bi.types.conversion_source

    out["source"] = capo_b2bi.types.conversion_source.serialize_aws_json_1_0(
        value["source"]
    )
    import capo_b2bi.types.conversion_target

    out["target"] = capo_b2bi.types.conversion_target.serialize_aws_json_1_0(
        value["target"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TestConversionRequest:
    out: TestConversionRequest = {}  # type: ignore[typeddict-item]
    if "source" in data:
        import capo_b2bi.types.conversion_source

        out["source"] = capo_b2bi.types.conversion_source.deserialize_aws_json_1_0(
            data["source"]
        )
    else:
        raise DeserializationError("TestConversionRequest.source required")
    if "target" in data:
        import capo_b2bi.types.conversion_target

        out["target"] = capo_b2bi.types.conversion_target.deserialize_aws_json_1_0(
            data["target"]
        )
    else:
        raise DeserializationError("TestConversionRequest.target required")
    return out
