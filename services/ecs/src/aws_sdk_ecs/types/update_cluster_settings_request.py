"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateClusterSettingsRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.cluster_settings
    import aws_sdk_ecs.types.string


class UpdateClusterSettingsRequest(TypedDict):
    cluster: "aws_sdk_ecs.types.string.String"
    """<p>The name of the cluster to modify the settings for.</p>"""
    settings: "aws_sdk_ecs.types.cluster_settings.ClusterSettings"
    """<p>The setting to use by default for a cluster. This parameter is used to turn on CloudWatch Container Insights for a cluster. If this value is specified, it overrides the <code>containerInsights</code> value set with <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutAccountSetting.html\">PutAccountSetting</a> or <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutAccountSettingDefault.html\">PutAccountSettingDefault</a>.</p> <important> <p>Currently, if you delete an existing cluster that does not have Container Insights turned on, and then create a new cluster with the same name with Container Insights tuned on, Container Insights will not actually be turned on. If you want to preserve the same name for your existing cluster and turn on Container Insights, you must wait 7 days before you can re-create it.</p> </important>"""
