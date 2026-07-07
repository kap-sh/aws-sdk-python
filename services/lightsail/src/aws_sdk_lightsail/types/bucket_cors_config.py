"""Generated from Smithy shape ``com.amazonaws.lightsail#BucketCorsConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.bucket_cors_rules


class BucketCorsConfig(TypedDict, closed=True):
    rules: NotRequired["aws_sdk_lightsail.types.bucket_cors_rules.BucketCorsRules"]
    """<p>A set of origins and methods (cross-origin access that you want to allow). You can add up to 20 rules to the configuration. The total size is limited to 64 KB.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BucketCorsConfig) -> dict:
    out: dict = {}
    if "rules" in value:
        import aws_sdk_lightsail.types.bucket_cors_rules

        out["rules"] = aws_sdk_lightsail.types.bucket_cors_rules.serialize_aws_json_1_1(
            value["rules"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BucketCorsConfig:
    out: BucketCorsConfig = {}  # type: ignore[typeddict-item]
    if "rules" in data:
        import aws_sdk_lightsail.types.bucket_cors_rules

        out["rules"] = (
            aws_sdk_lightsail.types.bucket_cors_rules.deserialize_aws_json_1_1(
                data["rules"]
            )
        )
    return out
