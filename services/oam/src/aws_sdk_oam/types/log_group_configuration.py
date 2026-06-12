"""Generated from Smithy shape ``com.amazonaws.oam#LogGroupConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_oam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_oam.types.logs_filter


class LogGroupConfiguration(TypedDict):
    filter: "aws_sdk_oam.types.logs_filter.LogsFilter"
    """<p>Use this field to specify which log groups are to share their log events with the monitoring account. Use the term <code>LogGroupName</code> and one or more of the following operands. Use single quotation marks (') around log group names. The matching of log group names is case sensitive. Each filter has a limit of five conditional operands. Conditional operands are <code>AND</code> and <code>OR</code>.</p> <ul> <li> <p> <code>=</code> and <code>!=</code> </p> </li> <li> <p> <code>AND</code> </p> </li> <li> <p> <code>OR</code> </p> </li> <li> <p> <code>LIKE</code> and <code>NOT LIKE</code>. These can be used only as prefix searches. Include a <code>%</code> at the end of the string that you want to search for and include.</p> </li> <li> <p> <code>IN</code> and <code>NOT IN</code>, using parentheses <code>( )</code> </p> </li> </ul> <p>Examples:</p> <ul> <li> <p> <code>LogGroupName IN ('This-Log-Group', 'Other-Log-Group')</code> includes only the log groups with names <code>This-Log-Group</code> and <code>Other-Log-Group</code>.</p> </li> <li> <p> <code>LogGroupName NOT IN ('Private-Log-Group', 'Private-Log-Group-2')</code> includes all log groups except the log groups with names <code>Private-Log-Group</code> and <code>Private-Log-Group-2</code>.</p> </li> <li> <p> <code>LogGroupName LIKE 'aws/lambda/%' OR LogGroupName LIKE 'AWSLogs%'</code> includes all log groups that have names that start with <code>aws/lambda/</code> or <code>AWSLogs</code>.</p> </li> </ul> <note> <p>If you are updating a link that uses filters, you can specify <code>*</code> as the only value for the <code>filter</code> parameter to delete the filter and share all log groups with the monitoring account.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogGroupConfiguration) -> dict:
    out: dict = {}
    out["Filter"] = value["filter"]
    return out


def deserialize_json(data: dict) -> LogGroupConfiguration:
    out: LogGroupConfiguration = {}  # type: ignore[typeddict-item]
    if "Filter" in data:
        out["filter"] = data["Filter"]
    else:
        raise DeserializationError("LogGroupConfiguration.filter required")
    return out
