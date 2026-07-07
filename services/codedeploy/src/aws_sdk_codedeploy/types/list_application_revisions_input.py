"""Generated from Smithy shape ``com.amazonaws.codedeploy#ListApplicationRevisionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codedeploy.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.application_name
    import aws_sdk_codedeploy.types.application_revision_sort_by
    import aws_sdk_codedeploy.types.list_state_filter_action
    import aws_sdk_codedeploy.types.next_token
    import aws_sdk_codedeploy.types.s3_bucket
    import aws_sdk_codedeploy.types.s3_key
    import aws_sdk_codedeploy.types.sort_order


class ListApplicationRevisionsInput(TypedDict, closed=True):
    application_name: "aws_sdk_codedeploy.types.application_name.ApplicationName"
    """<p> The name of an CodeDeploy application associated with the user or Amazon Web Services account. </p>"""
    sort_by: NotRequired[
        "aws_sdk_codedeploy.types.application_revision_sort_by.ApplicationRevisionSortBy"
    ]
    """<p>The column name to use to sort the list results:</p> <ul> <li> <p> <code>registerTime</code>: Sort by the time the revisions were registered with CodeDeploy.</p> </li> <li> <p> <code>firstUsedTime</code>: Sort by the time the revisions were first used in a deployment.</p> </li> <li> <p> <code>lastUsedTime</code>: Sort by the time the revisions were last used in a deployment.</p> </li> </ul> <p> If not specified or set to null, the results are returned in an arbitrary order. </p>"""
    sort_order: NotRequired["aws_sdk_codedeploy.types.sort_order.SortOrder"]
    """<p> The order in which to sort the list results: </p> <ul> <li> <p> <code>ascending</code>: ascending order.</p> </li> <li> <p> <code>descending</code>: descending order.</p> </li> </ul> <p>If not specified, the results are sorted in ascending order.</p> <p>If set to null, the results are sorted in an arbitrary order.</p>"""
    s3_bucket: NotRequired["aws_sdk_codedeploy.types.s3_bucket.S3Bucket"]
    """<p> An Amazon S3 bucket name to limit the search for revisions. </p> <p> If set to null, all of the user's buckets are searched. </p>"""
    s3_key_prefix: NotRequired["aws_sdk_codedeploy.types.s3_key.S3Key"]
    """<p> A key prefix for the set of Amazon S3 objects to limit the search for revisions. </p>"""
    deployed: NotRequired[
        "aws_sdk_codedeploy.types.list_state_filter_action.ListStateFilterAction"
    ]
    """<p> Whether to list revisions based on whether the revision is the target revision of a deployment group: </p> <ul> <li> <p> <code>include</code>: List revisions that are target revisions of a deployment group.</p> </li> <li> <p> <code>exclude</code>: Do not list revisions that are target revisions of a deployment group.</p> </li> <li> <p> <code>ignore</code>: List all revisions.</p> </li> </ul>"""
    next_token: NotRequired["aws_sdk_codedeploy.types.next_token.NextToken"]
    """<p>An identifier returned from the previous <code>ListApplicationRevisions</code> call. It can be used to return the next set of applications in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListApplicationRevisionsInput) -> dict:
    out: dict = {}
    out["applicationName"] = value["application_name"]
    if "sort_by" in value:
        import aws_sdk_codedeploy.types.application_revision_sort_by

        out["sortBy"] = (
            aws_sdk_codedeploy.types.application_revision_sort_by.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import aws_sdk_codedeploy.types.sort_order

        out["sortOrder"] = aws_sdk_codedeploy.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "s3_bucket" in value:
        out["s3Bucket"] = value["s3_bucket"]
    if "s3_key_prefix" in value:
        out["s3KeyPrefix"] = value["s3_key_prefix"]
    if "deployed" in value:
        import aws_sdk_codedeploy.types.list_state_filter_action

        out["deployed"] = (
            aws_sdk_codedeploy.types.list_state_filter_action.serialize_aws_json_1_1(
                value["deployed"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListApplicationRevisionsInput:
    out: ListApplicationRevisionsInput = {}  # type: ignore[typeddict-item]
    if "applicationName" in data:
        out["application_name"] = data["applicationName"]
    else:
        raise DeserializationError(
            "ListApplicationRevisionsInput.application_name required"
        )
    if "sortBy" in data:
        import aws_sdk_codedeploy.types.application_revision_sort_by

        out["sort_by"] = (
            aws_sdk_codedeploy.types.application_revision_sort_by.deserialize_aws_json_1_1(
                data["sortBy"]
            )
        )
    if "sortOrder" in data:
        import aws_sdk_codedeploy.types.sort_order

        out["sort_order"] = (
            aws_sdk_codedeploy.types.sort_order.deserialize_aws_json_1_1(
                data["sortOrder"]
            )
        )
    if "s3Bucket" in data:
        out["s3_bucket"] = data["s3Bucket"]
    if "s3KeyPrefix" in data:
        out["s3_key_prefix"] = data["s3KeyPrefix"]
    if "deployed" in data:
        import aws_sdk_codedeploy.types.list_state_filter_action

        out["deployed"] = (
            aws_sdk_codedeploy.types.list_state_filter_action.deserialize_aws_json_1_1(
                data["deployed"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
