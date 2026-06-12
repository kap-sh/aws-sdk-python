"""Generated from Smithy shape ``com.amazonaws.redshift#EnableLoggingMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.log_destination_type
    import aws_sdk_redshift.types.log_type_list
    import aws_sdk_redshift.types.s3_key_prefix_value
    import aws_sdk_redshift.types.string


class EnableLoggingMessage(TypedDict):
    cluster_identifier: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The identifier of the cluster on which logging is to be started.</p> <p>Example: <code>examplecluster</code> </p>"""
    bucket_name: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The name of an existing S3 bucket where the log files are to be stored.</p> <p>Constraints:</p> <ul> <li> <p>Must be in the same region as the cluster</p> </li> <li> <p>The cluster must have read bucket and put object permissions</p> </li> </ul>"""
    s3_key_prefix: NotRequired[
        "aws_sdk_redshift.types.s3_key_prefix_value.S3KeyPrefixValue"
    ]
    """<p>The prefix applied to the log file names.</p> <p>Valid characters are any letter from any language, any whitespace character, any numeric character, and the following characters: underscore (<code>_</code>), period (<code>.</code>), colon (<code>:</code>), slash (<code>/</code>), equal (<code>=</code>), plus (<code>+</code>), backslash (<code>\</code>), hyphen (<code>-</code>), at symbol (<code>@</code>).</p>"""
    log_destination_type: NotRequired[
        "aws_sdk_redshift.types.log_destination_type.LogDestinationType"
    ]
    """<p>The log destination type. An enum with possible values of <code>s3</code> and <code>cloudwatch</code>.</p>"""
    log_exports: NotRequired["aws_sdk_redshift.types.log_type_list.LogTypeList"]
    """<p>The collection of exported log types. Possible values are <code>connectionlog</code>, <code>useractivitylog</code>, and <code>userlog</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EnableLoggingMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cluster_identifier" in value:
        pairs.append((f"{prefix}.ClusterIdentifier", str(value["cluster_identifier"])))
    if "bucket_name" in value:
        pairs.append((f"{prefix}.BucketName", str(value["bucket_name"])))
    if "s3_key_prefix" in value:
        pairs.append((f"{prefix}.S3KeyPrefix", str(value["s3_key_prefix"])))
    if "log_destination_type" in value:
        import aws_sdk_redshift.types.log_destination_type

        aws_sdk_redshift.types.log_destination_type.serialize_query(
            value["log_destination_type"], pairs, f"{prefix}.LogDestinationType"
        )
    if "log_exports" in value:
        import aws_sdk_redshift.types.log_type_list

        aws_sdk_redshift.types.log_type_list.serialize_query(
            value["log_exports"], pairs, f"{prefix}.LogExports"
        )


def deserialize_query(el: Element) -> EnableLoggingMessage:
    out: EnableLoggingMessage = {}  # type: ignore[typeddict-item]
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_bucket_name = el.find("BucketName")
    if child_bucket_name is not None:
        out["bucket_name"] = str(child_bucket_name.text or "")
    child_s3_key_prefix = el.find("S3KeyPrefix")
    if child_s3_key_prefix is not None:
        out["s3_key_prefix"] = str(child_s3_key_prefix.text or "")
    child_log_destination_type = el.find("LogDestinationType")
    if child_log_destination_type is not None:
        import aws_sdk_redshift.types.log_destination_type

        out["log_destination_type"] = (
            aws_sdk_redshift.types.log_destination_type.deserialize_query(
                child_log_destination_type
            )
        )
    child_log_exports = el.find("LogExports")
    if child_log_exports is not None:
        import aws_sdk_redshift.types.log_type_list

        out["log_exports"] = aws_sdk_redshift.types.log_type_list.deserialize_query(
            child_log_exports
        )
    return out
