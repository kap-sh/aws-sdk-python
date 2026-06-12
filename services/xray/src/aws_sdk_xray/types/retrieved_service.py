"""Generated from Smithy shape ``com.amazonaws.xray#RetrievedService``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_xray.types.links_list
    import aws_sdk_xray.types.service


class RetrievedService(TypedDict):
    service: NotRequired["aws_sdk_xray.types.service.Service"]
    links: NotRequired["aws_sdk_xray.types.links_list.LinksList"]
    """<p> Relation between two 2 services. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrievedService) -> dict:
    out: dict = {}
    if "service" in value:
        import aws_sdk_xray.types.service

        out["Service"] = aws_sdk_xray.types.service.serialize_json(value["service"])
    if "links" in value:
        import aws_sdk_xray.types.links_list

        out["Links"] = aws_sdk_xray.types.links_list.serialize_json(value["links"])
    return out


def deserialize_json(data: dict) -> RetrievedService:
    out: RetrievedService = {}  # type: ignore[typeddict-item]
    if "Service" in data:
        import aws_sdk_xray.types.service

        out["service"] = aws_sdk_xray.types.service.deserialize_json(data["Service"])
    if "Links" in data:
        import aws_sdk_xray.types.links_list

        out["links"] = aws_sdk_xray.types.links_list.deserialize_json(data["Links"])
    return out
