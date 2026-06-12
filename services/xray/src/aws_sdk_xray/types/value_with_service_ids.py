"""Generated from Smithy shape ``com.amazonaws.xray#ValueWithServiceIds``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_xray.types.annotation_value
    import aws_sdk_xray.types.service_ids


class ValueWithServiceIds(TypedDict):
    annotation_value: NotRequired["aws_sdk_xray.types.annotation_value.AnnotationValue"]
    """<p>Values of the annotation.</p>"""
    service_ids: NotRequired["aws_sdk_xray.types.service_ids.ServiceIds"]
    """<p>Services to which the annotation applies.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValueWithServiceIds) -> dict:
    out: dict = {}
    if "annotation_value" in value:
        import aws_sdk_xray.types.annotation_value

        out["AnnotationValue"] = aws_sdk_xray.types.annotation_value.serialize_json(
            value["annotation_value"]
        )
    if "service_ids" in value:
        import aws_sdk_xray.types.service_ids

        out["ServiceIds"] = aws_sdk_xray.types.service_ids.serialize_json(
            value["service_ids"]
        )
    return out


def deserialize_json(data: dict) -> ValueWithServiceIds:
    out: ValueWithServiceIds = {}  # type: ignore[typeddict-item]
    if "AnnotationValue" in data:
        import aws_sdk_xray.types.annotation_value

        out["annotation_value"] = aws_sdk_xray.types.annotation_value.deserialize_json(
            data["AnnotationValue"]
        )
    if "ServiceIds" in data:
        import aws_sdk_xray.types.service_ids

        out["service_ids"] = aws_sdk_xray.types.service_ids.deserialize_json(
            data["ServiceIds"]
        )
    return out
