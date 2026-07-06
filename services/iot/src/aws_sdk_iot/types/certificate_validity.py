"""Generated from Smithy shape ``com.amazonaws.iot#CertificateValidity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.date_type


class CertificateValidity(TypedDict, closed=True):
    not_before: NotRequired["aws_sdk_iot.types.date_type.DateType"]
    """<p>The certificate is not valid before this date.</p>"""
    not_after: NotRequired["aws_sdk_iot.types.date_type.DateType"]
    """<p>The certificate is not valid after this date.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CertificateValidity) -> dict:
    out: dict = {}
    if "not_before" in value:
        import aws_sdk_iot.types.date_type

        out["notBefore"] = aws_sdk_iot.types.date_type.serialize_json(
            value["not_before"]
        )
    if "not_after" in value:
        import aws_sdk_iot.types.date_type

        out["notAfter"] = aws_sdk_iot.types.date_type.serialize_json(value["not_after"])
    return out


def deserialize_json(data: dict) -> CertificateValidity:
    out: CertificateValidity = {}  # type: ignore[typeddict-item]
    if "notBefore" in data:
        import aws_sdk_iot.types.date_type

        out["not_before"] = aws_sdk_iot.types.date_type.deserialize_json(
            data["notBefore"]
        )
    if "notAfter" in data:
        import aws_sdk_iot.types.date_type

        out["not_after"] = aws_sdk_iot.types.date_type.deserialize_json(
            data["notAfter"]
        )
    return out
