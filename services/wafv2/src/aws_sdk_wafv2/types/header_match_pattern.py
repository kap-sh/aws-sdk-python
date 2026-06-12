"""Generated from Smithy shape ``com.amazonaws.wafv2#HeaderMatchPattern``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.all
    import aws_sdk_wafv2.types.header_names


class HeaderMatchPattern(TypedDict):
    all: NotRequired["aws_sdk_wafv2.types.all.All"]
    """<p>Inspect all headers. </p>"""
    included_headers: NotRequired["aws_sdk_wafv2.types.header_names.HeaderNames"]
    """<p>Inspect only the headers that have a key that matches one of the strings specified here. </p>"""
    excluded_headers: NotRequired["aws_sdk_wafv2.types.header_names.HeaderNames"]
    """<p>Inspect only the headers whose keys don't match any of the strings specified here. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HeaderMatchPattern) -> dict:
    out: dict = {}
    if "all" in value:
        import aws_sdk_wafv2.types.all

        out["All"] = aws_sdk_wafv2.types.all.serialize_aws_json_1_1(value["all"])
    if "included_headers" in value:
        import aws_sdk_wafv2.types.header_names

        out["IncludedHeaders"] = (
            aws_sdk_wafv2.types.header_names.serialize_aws_json_1_1(
                value["included_headers"]
            )
        )
    if "excluded_headers" in value:
        import aws_sdk_wafv2.types.header_names

        out["ExcludedHeaders"] = (
            aws_sdk_wafv2.types.header_names.serialize_aws_json_1_1(
                value["excluded_headers"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HeaderMatchPattern:
    out: HeaderMatchPattern = {}  # type: ignore[typeddict-item]
    if "All" in data:
        import aws_sdk_wafv2.types.all

        out["all"] = aws_sdk_wafv2.types.all.deserialize_aws_json_1_1(data["All"])
    if "IncludedHeaders" in data:
        import aws_sdk_wafv2.types.header_names

        out["included_headers"] = (
            aws_sdk_wafv2.types.header_names.deserialize_aws_json_1_1(
                data["IncludedHeaders"]
            )
        )
    if "ExcludedHeaders" in data:
        import aws_sdk_wafv2.types.header_names

        out["excluded_headers"] = (
            aws_sdk_wafv2.types.header_names.deserialize_aws_json_1_1(
                data["ExcludedHeaders"]
            )
        )
    return out
