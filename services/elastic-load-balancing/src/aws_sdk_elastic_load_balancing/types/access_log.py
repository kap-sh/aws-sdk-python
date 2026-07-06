"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#AccessLog``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.access_log_enabled
    import aws_sdk_elastic_load_balancing.types.access_log_interval
    import aws_sdk_elastic_load_balancing.types.access_log_prefix
    import aws_sdk_elastic_load_balancing.types.s3_bucket_name


class AccessLog(TypedDict, closed=True):
    enabled: "aws_sdk_elastic_load_balancing.types.access_log_enabled.AccessLogEnabled"
    """<p>Specifies whether access logs are enabled for the load balancer.</p>"""
    s3_bucket_name: NotRequired[
        "aws_sdk_elastic_load_balancing.types.s3_bucket_name.S3BucketName"
    ]
    """<p>The name of the Amazon S3 bucket where the access logs are stored.</p>"""
    emit_interval: NotRequired[
        "aws_sdk_elastic_load_balancing.types.access_log_interval.AccessLogInterval"
    ]
    """<p>The interval for publishing the access logs. You can specify an interval of either 5 minutes or 60 minutes.</p> <p>Default: 60 minutes</p>"""
    s3_bucket_prefix: NotRequired[
        "aws_sdk_elastic_load_balancing.types.access_log_prefix.AccessLogPrefix"
    ]
    """<p>The logical hierarchy you created for your Amazon S3 bucket, for example <code>my-bucket-prefix/prod</code>. If the prefix is not provided, the log is placed at the root level of the bucket.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AccessLog, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append(
        (f"{prefix}.Enabled", "true" if value.get("enabled", False) else "false")
    )
    if "s3_bucket_name" in value:
        pairs.append((f"{prefix}.S3BucketName", str(value["s3_bucket_name"])))
    if "emit_interval" in value:
        pairs.append((f"{prefix}.EmitInterval", str(value["emit_interval"])))
    if "s3_bucket_prefix" in value:
        pairs.append((f"{prefix}.S3BucketPrefix", str(value["s3_bucket_prefix"])))


def deserialize_query(el: Element) -> AccessLog:
    out: AccessLog = {}  # type: ignore[typeddict-item]
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    else:
        out["enabled"] = False
    child_s3_bucket_name = el.find("S3BucketName")
    if child_s3_bucket_name is not None:
        out["s3_bucket_name"] = str(child_s3_bucket_name.text or "")
    child_emit_interval = el.find("EmitInterval")
    if child_emit_interval is not None:
        out["emit_interval"] = int(child_emit_interval.text or "")
    child_s3_bucket_prefix = el.find("S3BucketPrefix")
    if child_s3_bucket_prefix is not None:
        out["s3_bucket_prefix"] = str(child_s3_bucket_prefix.text or "")
    return out
