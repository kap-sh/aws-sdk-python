"""Generated from Smithy shape ``com.amazonaws.redshift#LoggingStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.boolean
    import capo_redshift.types.log_destination_type
    import capo_redshift.types.log_type_list
    import capo_redshift.types.s3_key_prefix_value
    import capo_redshift.types.string
    import capo_redshift.types.t_stamp


class LoggingStatus(TypedDict, closed=True):
    logging_enabled: NotRequired["capo_redshift.types.boolean.Boolean"]
    """<p> <code>true</code> if logging is on, <code>false</code> if logging is off.</p>"""
    bucket_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the S3 bucket where the log files are stored.</p>"""
    s3_key_prefix: NotRequired[
        "capo_redshift.types.s3_key_prefix_value.S3KeyPrefixValue"
    ]
    """<p>The prefix applied to the log file names.</p>"""
    last_successful_delivery_time: NotRequired["capo_redshift.types.t_stamp.TStamp"]
    """<p>The last time that logs were delivered.</p>"""
    last_failure_time: NotRequired["capo_redshift.types.t_stamp.TStamp"]
    """<p>The last time when logs failed to be delivered.</p>"""
    last_failure_message: NotRequired["capo_redshift.types.string.String"]
    """<p>The message indicating that logs failed to be delivered.</p>"""
    log_destination_type: NotRequired[
        "capo_redshift.types.log_destination_type.LogDestinationType"
    ]
    """<p>The log destination type. An enum with possible values of <code>s3</code> and <code>cloudwatch</code>.</p>"""
    log_exports: NotRequired["capo_redshift.types.log_type_list.LogTypeList"]
    """<p>The collection of exported log types. Possible values are <code>connectionlog</code>, <code>useractivitylog</code>, and <code>userlog</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: LoggingStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "logging_enabled" in value:
        pairs.append(
            (
                f"{prefix}.LoggingEnabled",
                "true" if value["logging_enabled"] else "false",
            )
        )
    if "bucket_name" in value:
        pairs.append((f"{prefix}.BucketName", str(value["bucket_name"])))
    if "s3_key_prefix" in value:
        pairs.append((f"{prefix}.S3KeyPrefix", str(value["s3_key_prefix"])))
    if "last_successful_delivery_time" in value:
        import capo_redshift.types.t_stamp

        capo_redshift.types.t_stamp.serialize_query(
            value["last_successful_delivery_time"],
            pairs,
            f"{prefix}.LastSuccessfulDeliveryTime",
        )
    if "last_failure_time" in value:
        import capo_redshift.types.t_stamp

        capo_redshift.types.t_stamp.serialize_query(
            value["last_failure_time"], pairs, f"{prefix}.LastFailureTime"
        )
    if "last_failure_message" in value:
        pairs.append(
            (f"{prefix}.LastFailureMessage", str(value["last_failure_message"]))
        )
    if "log_destination_type" in value:
        import capo_redshift.types.log_destination_type

        capo_redshift.types.log_destination_type.serialize_query(
            value["log_destination_type"], pairs, f"{prefix}.LogDestinationType"
        )
    if "log_exports" in value:
        import capo_redshift.types.log_type_list

        capo_redshift.types.log_type_list.serialize_query(
            value["log_exports"], pairs, f"{prefix}.LogExports"
        )


def deserialize_query(el: Element) -> LoggingStatus:
    out: LoggingStatus = {}  # type: ignore[typeddict-item]
    child_logging_enabled = el.find("LoggingEnabled")
    if child_logging_enabled is not None:
        out["logging_enabled"] = (child_logging_enabled.text or "").lower() == "true"
    child_bucket_name = el.find("BucketName")
    if child_bucket_name is not None:
        out["bucket_name"] = str(child_bucket_name.text or "")
    child_s3_key_prefix = el.find("S3KeyPrefix")
    if child_s3_key_prefix is not None:
        out["s3_key_prefix"] = str(child_s3_key_prefix.text or "")
    child_last_successful_delivery_time = el.find("LastSuccessfulDeliveryTime")
    if child_last_successful_delivery_time is not None:
        import capo_redshift.types.t_stamp

        out["last_successful_delivery_time"] = (
            capo_redshift.types.t_stamp.deserialize_query(
                child_last_successful_delivery_time
            )
        )
    child_last_failure_time = el.find("LastFailureTime")
    if child_last_failure_time is not None:
        import capo_redshift.types.t_stamp

        out["last_failure_time"] = capo_redshift.types.t_stamp.deserialize_query(
            child_last_failure_time
        )
    child_last_failure_message = el.find("LastFailureMessage")
    if child_last_failure_message is not None:
        out["last_failure_message"] = str(child_last_failure_message.text or "")
    child_log_destination_type = el.find("LogDestinationType")
    if child_log_destination_type is not None:
        import capo_redshift.types.log_destination_type

        out["log_destination_type"] = (
            capo_redshift.types.log_destination_type.deserialize_query(
                child_log_destination_type
            )
        )
    child_log_exports = el.find("LogExports")
    if child_log_exports is not None:
        import capo_redshift.types.log_type_list

        out["log_exports"] = capo_redshift.types.log_type_list.deserialize_query(
            child_log_exports
        )
    return out
