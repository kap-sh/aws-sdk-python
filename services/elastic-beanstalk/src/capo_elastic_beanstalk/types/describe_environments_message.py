"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#DescribeEnvironmentsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.application_name
    import capo_elastic_beanstalk.types.environment_id_list
    import capo_elastic_beanstalk.types.environment_names_list
    import capo_elastic_beanstalk.types.include_deleted
    import capo_elastic_beanstalk.types.include_deleted_back_to
    import capo_elastic_beanstalk.types.max_records
    import capo_elastic_beanstalk.types.token
    import capo_elastic_beanstalk.types.version_label


class DescribeEnvironmentsMessage(TypedDict, closed=True):
    application_name: NotRequired[
        "capo_elastic_beanstalk.types.application_name.ApplicationName"
    ]
    """<p>If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those that are associated with this application.</p>"""
    version_label: NotRequired[
        "capo_elastic_beanstalk.types.version_label.VersionLabel"
    ]
    """<p>If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those that are associated with this application version.</p>"""
    environment_ids: NotRequired[
        "capo_elastic_beanstalk.types.environment_id_list.EnvironmentIdList"
    ]
    """<p>If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those that have the specified IDs.</p>"""
    environment_names: NotRequired[
        "capo_elastic_beanstalk.types.environment_names_list.EnvironmentNamesList"
    ]
    """<p>If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those that have the specified names.</p>"""
    include_deleted: NotRequired[
        "capo_elastic_beanstalk.types.include_deleted.IncludeDeleted"
    ]
    """<p>Indicates whether to include deleted environments:</p> <p> <code>true</code>: Environments that have been deleted after <code>IncludedDeletedBackTo</code> are displayed.</p> <p> <code>false</code>: Do not include deleted environments.</p>"""
    included_deleted_back_to: NotRequired[
        "capo_elastic_beanstalk.types.include_deleted_back_to.IncludeDeletedBackTo"
    ]
    """<p> If specified when <code>IncludeDeleted</code> is set to <code>true</code>, then environments deleted after this date are displayed. </p>"""
    max_records: NotRequired["capo_elastic_beanstalk.types.max_records.MaxRecords"]
    """<p>For a paginated request. Specify a maximum number of environments to include in each response.</p> <p>If no <code>MaxRecords</code> is specified, all available environments are retrieved in a single response.</p>"""
    next_token: NotRequired["capo_elastic_beanstalk.types.token.Token"]
    """<p>For a paginated request. Specify a token from a previous response page to retrieve the next response page. All other parameter values must be identical to the ones specified in the initial request.</p> <p>If no <code>NextToken</code> is specified, the first page is retrieved.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeEnvironmentsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "application_name" in value:
        pairs.append((f"{prefix}.ApplicationName", str(value["application_name"])))
    if "version_label" in value:
        pairs.append((f"{prefix}.VersionLabel", str(value["version_label"])))
    if "environment_ids" in value:
        import capo_elastic_beanstalk.types.environment_id_list

        capo_elastic_beanstalk.types.environment_id_list.serialize_query(
            value["environment_ids"], pairs, f"{prefix}.EnvironmentIds"
        )
    if "environment_names" in value:
        import capo_elastic_beanstalk.types.environment_names_list

        capo_elastic_beanstalk.types.environment_names_list.serialize_query(
            value["environment_names"], pairs, f"{prefix}.EnvironmentNames"
        )
    if "include_deleted" in value:
        pairs.append(
            (
                f"{prefix}.IncludeDeleted",
                "true" if value["include_deleted"] else "false",
            )
        )
    if "included_deleted_back_to" in value:
        import capo_elastic_beanstalk.types.include_deleted_back_to

        capo_elastic_beanstalk.types.include_deleted_back_to.serialize_query(
            value["included_deleted_back_to"], pairs, f"{prefix}.IncludedDeletedBackTo"
        )
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> DescribeEnvironmentsMessage:
    out: DescribeEnvironmentsMessage = {}  # type: ignore[typeddict-item]
    child_application_name = el.find("ApplicationName")
    if child_application_name is not None:
        out["application_name"] = str(child_application_name.text or "")
    child_version_label = el.find("VersionLabel")
    if child_version_label is not None:
        out["version_label"] = str(child_version_label.text or "")
    child_environment_ids = el.find("EnvironmentIds")
    if child_environment_ids is not None:
        import capo_elastic_beanstalk.types.environment_id_list

        out["environment_ids"] = (
            capo_elastic_beanstalk.types.environment_id_list.deserialize_query(
                child_environment_ids
            )
        )
    child_environment_names = el.find("EnvironmentNames")
    if child_environment_names is not None:
        import capo_elastic_beanstalk.types.environment_names_list

        out["environment_names"] = (
            capo_elastic_beanstalk.types.environment_names_list.deserialize_query(
                child_environment_names
            )
        )
    child_include_deleted = el.find("IncludeDeleted")
    if child_include_deleted is not None:
        out["include_deleted"] = (child_include_deleted.text or "").lower() == "true"
    child_included_deleted_back_to = el.find("IncludedDeletedBackTo")
    if child_included_deleted_back_to is not None:
        import capo_elastic_beanstalk.types.include_deleted_back_to

        out["included_deleted_back_to"] = (
            capo_elastic_beanstalk.types.include_deleted_back_to.deserialize_query(
                child_included_deleted_back_to
            )
        )
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
