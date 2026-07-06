"""Generated from Smithy shape ``com.amazonaws.securityhub#FindingHistoryRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_security_finding_identifier
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.finding_history_update_source
    import aws_sdk_securityhub.types.finding_history_updates_list
    import aws_sdk_securityhub.types.next_token
    import aws_sdk_securityhub.types.timestamp


class FindingHistoryRecord(TypedDict, closed=True):
    finding_identifier: NotRequired[
        "aws_sdk_securityhub.types.aws_security_finding_identifier.AwsSecurityFindingIdentifier"
    ]
    update_time: NotRequired["aws_sdk_securityhub.types.timestamp.Timestamp"]
    r"""<p> A timestamp that indicates when Security Hub CSPM processed the updated finding record.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>"""
    finding_created: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p> Identifies whether the event marks the creation of a new finding. A value of <code>True</code> means that the finding is newly created. A value of <code>False</code> means that the finding isn’t newly created. </p>"""
    update_source: NotRequired[
        "aws_sdk_securityhub.types.finding_history_update_source.FindingHistoryUpdateSource"
    ]
    r"""<p> Identifies the source of the event that changed the finding. For example, an integrated Amazon Web Services service or third-party partner integration may call <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchImportFindings.html\"> <code>BatchImportFindings</code> </a>, or an Security Hub CSPM customer may call <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateFindings.html\"> <code>BatchUpdateFindings</code> </a>. </p>"""
    updates: NotRequired[
        "aws_sdk_securityhub.types.finding_history_updates_list.FindingHistoryUpdatesList"
    ]
    """<p> An array of objects that provides details about the finding change event, including the Amazon Web Services Security Finding Format (ASFF) field that changed, the value of the field before the change, and the value of the field after the change. </p>"""
    next_token: NotRequired["aws_sdk_securityhub.types.next_token.NextToken"]
    r"""<p> A token for pagination purposes. Provide this token in the subsequent request to <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetFindingsHistory.html\"> <code>GetFindingsHistory</code> </a> to get up to an additional 100 results of history for the same finding that you specified in your initial request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingHistoryRecord) -> dict:
    out: dict = {}
    if "finding_identifier" in value:
        import aws_sdk_securityhub.types.aws_security_finding_identifier

        out["FindingIdentifier"] = (
            aws_sdk_securityhub.types.aws_security_finding_identifier.serialize_json(
                value["finding_identifier"]
            )
        )
    if "update_time" in value:
        import aws_sdk_securityhub.types.timestamp

        out["UpdateTime"] = aws_sdk_securityhub.types.timestamp.serialize_json(
            value["update_time"]
        )
    if "finding_created" in value:
        out["FindingCreated"] = value["finding_created"]
    if "update_source" in value:
        import aws_sdk_securityhub.types.finding_history_update_source

        out["UpdateSource"] = (
            aws_sdk_securityhub.types.finding_history_update_source.serialize_json(
                value["update_source"]
            )
        )
    if "updates" in value:
        import aws_sdk_securityhub.types.finding_history_updates_list

        out["Updates"] = (
            aws_sdk_securityhub.types.finding_history_updates_list.serialize_json(
                value["updates"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> FindingHistoryRecord:
    out: FindingHistoryRecord = {}  # type: ignore[typeddict-item]
    if "FindingIdentifier" in data:
        import aws_sdk_securityhub.types.aws_security_finding_identifier

        out["finding_identifier"] = (
            aws_sdk_securityhub.types.aws_security_finding_identifier.deserialize_json(
                data["FindingIdentifier"]
            )
        )
    if "UpdateTime" in data:
        import aws_sdk_securityhub.types.timestamp

        out["update_time"] = aws_sdk_securityhub.types.timestamp.deserialize_json(
            data["UpdateTime"]
        )
    if "FindingCreated" in data:
        out["finding_created"] = data["FindingCreated"]
    if "UpdateSource" in data:
        import aws_sdk_securityhub.types.finding_history_update_source

        out["update_source"] = (
            aws_sdk_securityhub.types.finding_history_update_source.deserialize_json(
                data["UpdateSource"]
            )
        )
    if "Updates" in data:
        import aws_sdk_securityhub.types.finding_history_updates_list

        out["updates"] = (
            aws_sdk_securityhub.types.finding_history_updates_list.deserialize_json(
                data["Updates"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
