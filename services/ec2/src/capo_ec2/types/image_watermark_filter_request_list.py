"""Generated from Smithy shape ``com.amazonaws.ec2#ImageWatermarkFilterRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.image_watermark_filter_request

ImageWatermarkFilterRequestList: TypeAlias = list[
    "capo_ec2.types.image_watermark_filter_request.ImageWatermarkFilterRequest"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImageWatermarkFilterRequestList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.image_watermark_filter_request

        capo_ec2.types.image_watermark_filter_request.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> ImageWatermarkFilterRequestList:
    import capo_ec2.types.image_watermark_filter_request

    out: ImageWatermarkFilterRequestList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.image_watermark_filter_request.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> ImageWatermarkFilterRequestList:
    import capo_ec2.types.image_watermark_filter_request

    out: ImageWatermarkFilterRequestList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.image_watermark_filter_request.deserialize_ec2_query(child)
        )
    return out
