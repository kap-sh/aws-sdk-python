"""Generated from Smithy shape ``com.amazonaws.ecs#ClusterSetting``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.cluster_setting_name
    import aws_sdk_ecs.types.string


class ClusterSetting(TypedDict):
    name: NotRequired["aws_sdk_ecs.types.cluster_setting_name.ClusterSettingName"]
    """<p>The name of the cluster setting. The value is <code>containerInsights</code>.</p>"""
    value: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The value to set for the cluster setting. The supported values are <code>enhanced</code>, <code>enabled</code>, and <code>disabled</code>. </p> <p>To use Container Insights with enhanced observability, set the <code>containerInsights</code> account setting to <code>enhanced</code>.</p> <p>To use Container Insights, set the <code>containerInsights</code> account setting to <code>enabled</code>.</p> <p>If a cluster value is specified, it will override the <code>containerInsights</code> value set with <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutAccountSetting.html\">PutAccountSetting</a> or <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutAccountSettingDefault.html\">PutAccountSettingDefault</a>.</p>"""
