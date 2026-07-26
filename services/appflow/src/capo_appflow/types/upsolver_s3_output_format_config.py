"""Generated from Smithy shape ``com.amazonaws.appflow#UpsolverS3OutputFormatConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appflow.types.aggregation_config
    import capo_appflow.types.file_type
    import capo_appflow.types.prefix_config


class UpsolverS3OutputFormatConfig(TypedDict, closed=True):
    file_type: NotRequired["capo_appflow.types.file_type.FileType"]
    """<p> Indicates the file type that Amazon AppFlow places in the Upsolver Amazon S3 bucket. </p>"""
    prefix_config: "capo_appflow.types.prefix_config.PrefixConfig"
    aggregation_config: NotRequired[
        "capo_appflow.types.aggregation_config.AggregationConfig"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpsolverS3OutputFormatConfig) -> dict:
    out: dict = {}
    if "file_type" in value:
        import capo_appflow.types.file_type

        out["fileType"] = capo_appflow.types.file_type.serialize_json(
            value["file_type"]
        )
    import capo_appflow.types.prefix_config

    out["prefixConfig"] = capo_appflow.types.prefix_config.serialize_json(
        value["prefix_config"]
    )
    if "aggregation_config" in value:
        import capo_appflow.types.aggregation_config

        out["aggregationConfig"] = capo_appflow.types.aggregation_config.serialize_json(
            value["aggregation_config"]
        )
    return out


def deserialize_json(data: dict) -> UpsolverS3OutputFormatConfig:
    out: UpsolverS3OutputFormatConfig = {}  # type: ignore[typeddict-item]
    if "fileType" in data:
        import capo_appflow.types.file_type

        out["file_type"] = capo_appflow.types.file_type.deserialize_json(
            data["fileType"]
        )
    if "prefixConfig" in data:
        import capo_appflow.types.prefix_config

        out["prefix_config"] = capo_appflow.types.prefix_config.deserialize_json(
            data["prefixConfig"]
        )
    else:
        raise DeserializationError(
            "UpsolverS3OutputFormatConfig.prefix_config required"
        )
    if "aggregationConfig" in data:
        import capo_appflow.types.aggregation_config

        out["aggregation_config"] = (
            capo_appflow.types.aggregation_config.deserialize_json(
                data["aggregationConfig"]
            )
        )
    return out
