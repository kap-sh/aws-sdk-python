"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#DescribeApplicationVersionsMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.application_name
    import aws_sdk_elastic_beanstalk.types.max_records
    import aws_sdk_elastic_beanstalk.types.token
    import aws_sdk_elastic_beanstalk.types.version_labels_list


class DescribeApplicationVersionsMessage(TypedDict):
    application_name: NotRequired[
        "aws_sdk_elastic_beanstalk.types.application_name.ApplicationName"
    ]
    """<p>Specify an application name to show only application versions for that application.</p>"""
    version_labels: NotRequired[
        "aws_sdk_elastic_beanstalk.types.version_labels_list.VersionLabelsList"
    ]
    """<p>Specify a version label to show a specific application version.</p>"""
    max_records: NotRequired["aws_sdk_elastic_beanstalk.types.max_records.MaxRecords"]
    """<p>For a paginated request. Specify a maximum number of application versions to include in each response.</p> <p>If no <code>MaxRecords</code> is specified, all available application versions are retrieved in a single response.</p>"""
    next_token: NotRequired["aws_sdk_elastic_beanstalk.types.token.Token"]
    """<p>For a paginated request. Specify a token from a previous response page to retrieve the next response page. All other parameter values must be identical to the ones specified in the initial request.</p> <p>If no <code>NextToken</code> is specified, the first page is retrieved.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeApplicationVersionsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "application_name" in value:
        pairs.append((f"{prefix}.ApplicationName", str(value["application_name"])))
    if "version_labels" in value:
        import aws_sdk_elastic_beanstalk.types.version_labels_list

        aws_sdk_elastic_beanstalk.types.version_labels_list.serialize_query(
            value["version_labels"], pairs, f"{prefix}.VersionLabels"
        )
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> DescribeApplicationVersionsMessage:
    out: DescribeApplicationVersionsMessage = {}  # type: ignore[typeddict-item]
    child_application_name = el.find("ApplicationName")
    if child_application_name is not None:
        out["application_name"] = str(child_application_name.text or "")
    child_version_labels = el.find("VersionLabels")
    if child_version_labels is not None:
        import aws_sdk_elastic_beanstalk.types.version_labels_list

        out["version_labels"] = (
            aws_sdk_elastic_beanstalk.types.version_labels_list.deserialize_query(
                child_version_labels
            )
        )
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
