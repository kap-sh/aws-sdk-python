"""Generated from Smithy shape ``com.amazonaws.quicksight#StaticFileSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.static_file_s3_source_options
    import capo_quicksight.types.static_file_url_source_options


class StaticFileSource(TypedDict, closed=True):
    url_options: NotRequired[
        "capo_quicksight.types.static_file_url_source_options.StaticFileUrlSourceOptions"
    ]
    """<p>The structure that contains the URL to download the static file from.</p>"""
    s3_options: NotRequired[
        "capo_quicksight.types.static_file_s3_source_options.StaticFileS3SourceOptions"
    ]
    """<p>The structure that contains the Amazon S3 location to download the static file from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StaticFileSource) -> dict:
    out: dict = {}
    if "url_options" in value:
        import capo_quicksight.types.static_file_url_source_options

        out["UrlOptions"] = (
            capo_quicksight.types.static_file_url_source_options.serialize_json(
                value["url_options"]
            )
        )
    if "s3_options" in value:
        import capo_quicksight.types.static_file_s3_source_options

        out["S3Options"] = (
            capo_quicksight.types.static_file_s3_source_options.serialize_json(
                value["s3_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> StaticFileSource:
    out: StaticFileSource = {}  # type: ignore[typeddict-item]
    if "UrlOptions" in data:
        import capo_quicksight.types.static_file_url_source_options

        out["url_options"] = (
            capo_quicksight.types.static_file_url_source_options.deserialize_json(
                data["UrlOptions"]
            )
        )
    if "S3Options" in data:
        import capo_quicksight.types.static_file_s3_source_options

        out["s3_options"] = (
            capo_quicksight.types.static_file_s3_source_options.deserialize_json(
                data["S3Options"]
            )
        )
    return out
