"""Generated from Smithy shape ``com.amazonaws.devopsguru#TagHealth``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.analyzed_resource_count
    import capo_devops_guru.types.app_boundary_key
    import capo_devops_guru.types.insight_health
    import capo_devops_guru.types.tag_value


class TagHealth(TypedDict, closed=True):
    app_boundary_key: NotRequired[
        "capo_devops_guru.types.app_boundary_key.AppBoundaryKey"
    ]
    """<p>An Amazon Web Services tag <i>key</i> that is used to identify the Amazon Web Services resources that DevOps Guru analyzes. All Amazon Web Services resources in your account and Region tagged with this <i>key</i> make up your DevOps Guru application and analysis boundary.</p> <important> <p>The string used for a <i>key</i> in a tag that you use to define your resource coverage must begin with the prefix <code>Devops-guru-</code>. The tag <i>key</i> might be <code>DevOps-Guru-deployment-application</code> or <code>devops-guru-rds-application</code>. When you create a <i>key</i>, the case of characters in the <i>key</i> can be whatever you choose. After you create a <i>key</i>, it is case-sensitive. For example, DevOps Guru works with a <i>key</i> named <code>devops-guru-rds</code> and a <i>key</i> named <code>DevOps-Guru-RDS</code>, and these act as two different <i>keys</i>. Possible <i>key</i>/<i>value</i> pairs in your application might be <code>Devops-Guru-production-application/RDS</code> or <code>Devops-Guru-production-application/containers</code>.</p> </important>"""
    tag_value: NotRequired["capo_devops_guru.types.tag_value.TagValue"]
    """<p>The value in an Amazon Web Services tag.</p> <p>The tag's <i>value</i> is an optional field used to associate a string with the tag <i>key</i> (for example, <code>111122223333</code>, <code>Production</code>, or a team name). The <i>key</i> and <i>value</i> are the tag's <i>key</i> pair. Omitting the tag <i>value</i> is the same as using an empty string. Like tag <i>keys</i>, tag <i>values</i> are case-sensitive. You can specify a maximum of 256 characters for a tag value.</p>"""
    insight: NotRequired["capo_devops_guru.types.insight_health.InsightHealth"]
    """<p>Information about the health of the Amazon Web Services resources in your account that are specified by an Amazon Web Services tag, including the number of open proactive, open reactive insights, and the Mean Time to Recover (MTTR) of closed insights. </p>"""
    analyzed_resource_count: NotRequired[
        "capo_devops_guru.types.analyzed_resource_count.AnalyzedResourceCount"
    ]
    """<p> Number of resources that DevOps Guru is monitoring in your account that are specified by an Amazon Web Services tag. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagHealth) -> dict:
    out: dict = {}
    if "app_boundary_key" in value:
        out["AppBoundaryKey"] = value["app_boundary_key"]
    if "tag_value" in value:
        out["TagValue"] = value["tag_value"]
    if "insight" in value:
        import capo_devops_guru.types.insight_health

        out["Insight"] = capo_devops_guru.types.insight_health.serialize_json(
            value["insight"]
        )
    if "analyzed_resource_count" in value:
        out["AnalyzedResourceCount"] = value["analyzed_resource_count"]
    return out


def deserialize_json(data: dict) -> TagHealth:
    out: TagHealth = {}  # type: ignore[typeddict-item]
    if "AppBoundaryKey" in data:
        out["app_boundary_key"] = data["AppBoundaryKey"]
    if "TagValue" in data:
        out["tag_value"] = data["TagValue"]
    if "Insight" in data:
        import capo_devops_guru.types.insight_health

        out["insight"] = capo_devops_guru.types.insight_health.deserialize_json(
            data["Insight"]
        )
    if "AnalyzedResourceCount" in data:
        out["analyzed_resource_count"] = data["AnalyzedResourceCount"]
    return out
