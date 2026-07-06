"""Generated from Smithy shape ``com.amazonaws.mediatailor#CdnConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__string


class CdnConfiguration(TypedDict, closed=True):
    ad_segment_url_prefix: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>A non-default content delivery network (CDN) to serve ad segments. By default, AWS Elemental MediaTailor uses Amazon CloudFront with default cache settings as its CDN for ad segments. To set up an alternate CDN, create a rule in your CDN for the origin ads.mediatailor.<i>&lt;region&gt;</i>.amazonaws.com. Then specify the rule's name in this <code>AdSegmentUrlPrefix</code>. When AWS Elemental MediaTailor serves a manifest, it reports your CDN as the source for ad segments.</p>"""
    content_segment_url_prefix: NotRequired[
        "aws_sdk_mediatailor.types.__string.__string"
    ]
    """<p>A content delivery network (CDN) to cache content segments, so that content requests don’t always have to go to the origin server. First, create a rule in your CDN for the content segment origin server. Then specify the rule's name in this <code>ContentSegmentUrlPrefix</code>. When AWS Elemental MediaTailor serves a manifest, it reports your CDN as the source for content segments.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CdnConfiguration) -> dict:
    out: dict = {}
    if "ad_segment_url_prefix" in value:
        out["AdSegmentUrlPrefix"] = value["ad_segment_url_prefix"]
    if "content_segment_url_prefix" in value:
        out["ContentSegmentUrlPrefix"] = value["content_segment_url_prefix"]
    return out


def deserialize_json(data: dict) -> CdnConfiguration:
    out: CdnConfiguration = {}  # type: ignore[typeddict-item]
    if "AdSegmentUrlPrefix" in data:
        out["ad_segment_url_prefix"] = data["AdSegmentUrlPrefix"]
    if "ContentSegmentUrlPrefix" in data:
        out["content_segment_url_prefix"] = data["ContentSegmentUrlPrefix"]
    return out
