"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ExportingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.s3_exporting_config


class ExportingConfig(TypedDict, closed=True):
    s3_exporting: NotRequired[
        "capo_customer_profiles.types.s3_exporting_config.S3ExportingConfig"
    ]
    """<p>The S3 location where Identity Resolution Jobs write result files.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportingConfig) -> dict:
    out: dict = {}
    if "s3_exporting" in value:
        import capo_customer_profiles.types.s3_exporting_config

        out["S3Exporting"] = (
            capo_customer_profiles.types.s3_exporting_config.serialize_json(
                value["s3_exporting"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExportingConfig:
    out: ExportingConfig = {}  # type: ignore[typeddict-item]
    if "S3Exporting" in data:
        import capo_customer_profiles.types.s3_exporting_config

        out["s3_exporting"] = (
            capo_customer_profiles.types.s3_exporting_config.deserialize_json(
                data["S3Exporting"]
            )
        )
    return out
