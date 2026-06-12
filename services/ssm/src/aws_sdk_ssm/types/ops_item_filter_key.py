"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemFilterKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

OpsItemFilterKey: TypeAlias = Literal[
    "Status",
    "CreatedBy",
    "Source",
    "Priority",
    "Title",
    "OpsItemId",
    "CreatedTime",
    "LastModifiedTime",
    "ActualStartTime",
    "ActualEndTime",
    "PlannedStartTime",
    "PlannedEndTime",
    "OperationalData",
    "OperationalDataKey",
    "OperationalDataValue",
    "ResourceId",
    "AutomationId",
    "Category",
    "Severity",
    "OpsItemType",
    "AccessRequestByRequesterArn",
    "AccessRequestByRequesterId",
    "AccessRequestByApproverArn",
    "AccessRequestByApproverId",
    "AccessRequestBySourceAccountId",
    "AccessRequestBySourceOpsItemId",
    "AccessRequestBySourceRegion",
    "AccessRequestByIsReplica",
    "AccessRequestByTargetResourceId",
    "ChangeRequestByRequesterArn",
    "ChangeRequestByRequesterName",
    "ChangeRequestByApproverArn",
    "ChangeRequestByApproverName",
    "ChangeRequestByTemplate",
    "ChangeRequestByTargetsResourceGroup",
    "InsightByType",
    "AccountId",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Status",
        "CreatedBy",
        "Source",
        "Priority",
        "Title",
        "OpsItemId",
        "CreatedTime",
        "LastModifiedTime",
        "ActualStartTime",
        "ActualEndTime",
        "PlannedStartTime",
        "PlannedEndTime",
        "OperationalData",
        "OperationalDataKey",
        "OperationalDataValue",
        "ResourceId",
        "AutomationId",
        "Category",
        "Severity",
        "OpsItemType",
        "AccessRequestByRequesterArn",
        "AccessRequestByRequesterId",
        "AccessRequestByApproverArn",
        "AccessRequestByApproverId",
        "AccessRequestBySourceAccountId",
        "AccessRequestBySourceOpsItemId",
        "AccessRequestBySourceRegion",
        "AccessRequestByIsReplica",
        "AccessRequestByTargetResourceId",
        "ChangeRequestByRequesterArn",
        "ChangeRequestByRequesterName",
        "ChangeRequestByApproverArn",
        "ChangeRequestByApproverName",
        "ChangeRequestByTemplate",
        "ChangeRequestByTargetsResourceGroup",
        "InsightByType",
        "AccountId",
    )
)


def serialize_aws_json_1_1(value: OpsItemFilterKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OpsItemFilterKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OpsItemFilterKey value: {data!r}")
    return cast(OpsItemFilterKey, data)
