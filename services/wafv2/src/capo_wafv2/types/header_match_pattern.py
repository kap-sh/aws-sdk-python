"""Generated from Smithy shape ``com.amazonaws.wafv2#HeaderMatchPattern``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.all
    import capo_wafv2.types.header_names


class HeaderMatchPattern(TypedDict, closed=True):
    all: NotRequired["capo_wafv2.types.all.All"]
    """<p>Inspect all headers. </p>"""
    included_headers: NotRequired["capo_wafv2.types.header_names.HeaderNames"]
    """<p>Inspect only the headers that have a key that matches one of the strings specified here. </p>"""
    excluded_headers: NotRequired["capo_wafv2.types.header_names.HeaderNames"]
    """<p>Inspect only the headers whose keys don't match any of the strings specified here. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HeaderMatchPattern) -> dict:
    out: dict = {}
    if "all" in value:
        import capo_wafv2.types.all

        out["All"] = capo_wafv2.types.all.serialize_aws_json_1_1(value["all"])
    if "included_headers" in value:
        import capo_wafv2.types.header_names

        out["IncludedHeaders"] = capo_wafv2.types.header_names.serialize_aws_json_1_1(
            value["included_headers"]
        )
    if "excluded_headers" in value:
        import capo_wafv2.types.header_names

        out["ExcludedHeaders"] = capo_wafv2.types.header_names.serialize_aws_json_1_1(
            value["excluded_headers"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HeaderMatchPattern:
    out: HeaderMatchPattern = {}  # type: ignore[typeddict-item]
    if "All" in data:
        import capo_wafv2.types.all

        out["all"] = capo_wafv2.types.all.deserialize_aws_json_1_1(data["All"])
    if "IncludedHeaders" in data:
        import capo_wafv2.types.header_names

        out["included_headers"] = (
            capo_wafv2.types.header_names.deserialize_aws_json_1_1(
                data["IncludedHeaders"]
            )
        )
    if "ExcludedHeaders" in data:
        import capo_wafv2.types.header_names

        out["excluded_headers"] = (
            capo_wafv2.types.header_names.deserialize_aws_json_1_1(
                data["ExcludedHeaders"]
            )
        )
    return out
